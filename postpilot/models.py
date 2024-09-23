from django.db import models
from django.contrib.auth.models import User

class ScheduledPost(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='')
    caption = models.TextField()
    scheduled_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} scheduled for {self.scheduled_time}"