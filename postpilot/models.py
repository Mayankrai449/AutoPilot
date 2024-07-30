from django.db import models
from django.contrib.auth.models import User

class ScheduledPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='instagram_posts/')
    caption = models.TextField()
    scheduled_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)