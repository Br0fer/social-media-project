from django.db import models
from profiles.models import Profile

# Create your models here.


class FriendRequest(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friend_requests_send")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friend_requests_receive")
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["sender", "receiver"], name="unique_friend_request"),
            models.CheckConstraint(check=~models.Q(sender=models.F("receiver")), name="no_self_friend_request"),
        ]

    def __str__(self):
        return f"{self.sender.username} send friend request to {self.receiver.username}"
