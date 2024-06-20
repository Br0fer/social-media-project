from django.db import models
from profiles.models import Profile

# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="groups")
    created_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="memberships")
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")
