from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    likes = models.ManyToManyField('social_network.Post')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

