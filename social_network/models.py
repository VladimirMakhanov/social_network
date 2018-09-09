from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, password):
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    # first_name = models.CharField(max_length=255, null=False, blank=False)
    # last_name = models.CharField(max_length=255, null=False, blank=True)
    # email = models.EmailField(null=False, blank=False, unique=True)
    # password = models.CharField(max_length=255, null=False, blank=False)
    likes = models.ManyToManyField('social_network.Post')
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # def save(self, *args, **kwargs):
    #
    #     super(User, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class BearerTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    access_token = models.CharField(max_length=255, null=False, blank=False)
    lifetime_access_token = models.DateTimeField()
    refresh_token = models.CharField(max_length=255, null=False, blank=False)
    lifetime_refresh_token = models.DateTimeField()

