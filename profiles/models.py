from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    pfp = models.FileField(upload_to="users_pfp")
    username = models.CharField(max_length=80)
    bio = models.CharField(max_length=500)
    status = models.CharField(max_length=60)


class Friendship(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends_from")
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends_to")


class Subscriber(models.Model):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscriptions")
    account = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscribers")
