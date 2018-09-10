from urllib3 import exceptions as urllib3_exceptions
from requests import exceptions as requests_exceptions
from rest_framework import serializers
from pyhunter import PyHunter

hunter = PyHunter('29339a18e1062328d4bc8bc82eac1a42e1c532e4')


def verify_email(email):
    try:
        res = hunter.email_verifier(email)

    except urllib3_exceptions.HTTPError:
        raise serializers.ValidationError('Email is invalid')

    except requests_exceptions.HTTPError:
        raise serializers.ValidationError('Email is invalid')

    except Exception as e:
        raise serializers.ValidationError(e)

    else:
        return res