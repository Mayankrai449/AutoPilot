from celery import shared_task
from .models import ScheduledPost
import requests
from datetime import datetime
from django.conf import settings

@shared_task
def publish_scheduled_posts():
    now = datetime.now()
    scheduled_posts = ScheduledPost.objects.filter(scheduled_time__lte=now, published=False)
    for post in scheduled_posts:
        image_url = f'{settings.MEDIA_URL}{post.image}'
        response = requests.post(
            f'https://graph.facebook.com/v14.0/{user_id}/media',
            params={
                'image_url': image_url,
                'caption': post.caption,
                'access_token': user_access_token,
            }
        )
        if response.status_code == 200:
            post.published = True
            post.save()
