from pprint import pprint
import logging
import clearbit
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict
from social_network.models import User
from social_network.serializers import ClearbitInfoSerializer


def normalize(data, _key=''):
    result = {}
    for key, value in data.items():
        k = f'{_key}_{key}' if _key != '' else key
        if type(value) == dict:
            # pprint({value: type(value), 'equal': value == []})
            # if value == []:
            #     tmp = {k: ''}
            # else:
            tmp = normalize(value, _key=k)
            result.update(tmp)
        else:
            result[k] = value if value else ''
    return result


@receiver(post_save, sender=User, dispatch_uid='get_info_from_cleatbit')
def get_info_from_clearbit(sender, instance, **kwargs):
    clearbit.key = 'sk_0045f533d191775f134fb6d95c2106ba'
    response = clearbit.Enrichment.find(email=instance.email)

    try:
        if response['person'] is not None:
            data = normalize(response['person'])
            data.update({'user': instance.pk})
            cb = ClearbitInfoSerializer(data=data)

            if cb.is_valid():
                cb.save()

    except TypeError:
        pass

    finally:
        pass


post_save.connect(get_info_from_clearbit, User)
