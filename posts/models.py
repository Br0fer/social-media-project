from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to="posts_images")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_on_post")
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comments")

    def __str__(self):
        return f"Comment by {self.created_by.username} under {self.related_post.title} post"


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user.username} liked {self.post.title} post"
