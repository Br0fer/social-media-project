from django.db import models
from accounts.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    pfp = models.ImageField(upload_to="users_pfp")
    username = models.CharField(max_length=80)
    bio = models.CharField(max_length=500)
    status = models.CharField(max_length=60)
    banner = models.ImageField(upload_to="users_banners")

    def __str__(self):
        return self.username


class Friendship(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends_from")
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends_to")

    def __str__(self):
        return f"{self.user1.username} is friends with {self.user2.username}"


class Subscriber(models.Model):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscriptions")
    account = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscribers")

    def __str__(self):
        return f"{self.subscriber.username} subscribed to {self.account.username}"
