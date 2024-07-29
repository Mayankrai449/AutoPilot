from celery import shared_task
from .models import ScheduledPost
from datetime import datetime
import requests
from decouple import config

@shared_task
def publish_scheduled_posts():
    now = datetime.now()
    scheduled_posts = ScheduledPost.objects.filter(publish_time__lte=now, published=False)
    
    for post in scheduled_posts:
        response = publish_to_instagram(post)
        
        if response.status_code == 200:
            post.published = True
            post.save()
        else:
            print(f"Failed to publish post {post.id}: {response.content}")

def publish_to_instagram(post):
    url = f"https://graph.facebook.com/v11.0/{post.instagram_user_id}/media"
    payload = {
        'image_url': post.image_url,
        'caption': post.caption,
        'access_token': config('INSTAGRAM_ACCESS_TOKEN')
    }
    response = requests.post(url, data=payload)
    return response
