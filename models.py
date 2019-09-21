from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#this function is supposed to create a token for a new user
#not sure it works yet. remember to confirm that it does
#i even added a function that retrieves the token to the url
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Builds(models.Model):
    username = models.CharField(max_length=255)
    build = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Inks(models.Model):
    username = models.CharField(max_length=255)
    ink = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Follows(models.Model):
    followers = models.CharField(max_length=255)
    following = models.CharField(max_length=255)

    def __str__(self):
        return self.followers
