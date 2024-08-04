from django.db import models
from profiles.models import Profile

# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="groups")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="memberships")
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.user.username} is member of {self.group.title} group"

    class Meta:
        unique_together = ("user", "group")


class Community(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="communities")
    created_at = models.DateTimeField(auto_now_add=True)


class Viewer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="views")
    is_admin = models.BooleanField(default=False)
    community = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="viewers")
