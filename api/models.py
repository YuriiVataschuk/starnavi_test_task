import datetime

from django.db import models

from user.models import User


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Created at {self.created} by {self.user}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(Like, related_name="posts", null=True, blank=True)
