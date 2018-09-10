from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


class SocialNetworkConfig(AppConfig):
    name = 'social_network'

    def ready(self):
        print('Import signals')
        import social_network.signals



