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

class ClearbitInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name_givenName = models.CharField(max_length=255, null=True, blank=True)
    name_familyName = models.CharField(max_length=255, null=True, blank=True)
    name_fullName = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    timeZone = models.CharField(max_length=255, null=True, blank=True)
    utcOffset = models.CharField(max_length=255, null=True, blank=True)
    get_city = models.CharField(max_length=255, null=True, blank=True)
    get_state = models.CharField(max_length=255, null=True, blank=True)
    get_country = models.CharField(max_length=255, null=True, blank=True)
    get_lat = models.FloatField(null=True, blank=True)
    get_lng = models.FloatField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    employment_name = models.CharField(max_length=255, null=True, blank=True)
    employment_title = models.CharField(max_length=255, null=True, blank=True)
    employment_role = models.CharField(max_length=255, null=True, blank=True)
    employment_seniority = models.CharField(max_length=255, null=True, blank=True)
    employment_domain = models.CharField(max_length=255, null=True, blank=True)
    facebook_handle = models.CharField(max_length=255, null=True, blank=True)
    github_handle = models.CharField(max_length=255, null=True, blank=True)
    github_id = models.CharField(max_length=255, null=True, blank=True)
    github_avatar = models.CharField(max_length=255, null=True, blank=True)
    github_company = models.CharField(max_length=255, null=True, blank=True)
    github_blog = models.CharField(max_length=255, null=True, blank=True)
    github_followers = models.CharField(max_length=255, null=True, blank=True)
    github_following = models.CharField(max_length=255, null=True, blank=True)
    twitter_handle = models.CharField(max_length=255, null=True, blank=True)
    twitter_id = models.CharField(max_length=255, null=True, blank=True)
    twitter_followers = models.CharField(max_length=255, null=True, blank=True)
    twitter_following = models.CharField(max_length=255, null=True, blank=True)
    twitter_location = models.CharField(max_length=255, null=True, blank=True)
    twitter_site = models.CharField(max_length=255, null=True, blank=True)
    twitter_statuses = models.CharField(max_length=255, null=True, blank=True)
    twitter_favorites = models.CharField(max_length=255, null=True, blank=True)
    twitter_avatar = models.CharField(max_length=255, null=True, blank=True)
    linkedin_handle = models.CharField(max_length=255, null=True, blank=True)
    googleplus_handle = models.CharField(max_length=255, null=True, blank=True)
    gravatar_handle = models.CharField(max_length=255, null=True, blank=True)
    gravatar_urls = models.CharField(max_length=255, null=True, blank=True)
    gravatar_avatar = models.CharField(max_length=255, null=True, blank=True)
    gravatar_avatars = models.CharField(max_length=255, null=True, blank=True)
    fuzzy = models.NullBooleanField(null=True, blank=True)
    emailProvider = models.NullBooleanField(null=True, blank=True)
    indexedAt = models.CharField(max_length=255, null=True, blank=True)


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

