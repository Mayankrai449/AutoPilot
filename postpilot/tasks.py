import logging
from celery import shared_task
from datetime import datetime
from .models import ScheduledPost
from .instagram_utils import create_media_object, publish_media_object
import pytz

logger = logging.getLogger(__name__)

@shared_task
def publish_scheduled_posts():
    now = datetime.now(pytz.timezone('Asia/Kolkata'))
    scheduled_posts = ScheduledPost.objects.filter(is_published=False)

    logger.info("Upload Started")
    
    for post in scheduled_posts:
        try:
            logger.info(f"Creating media object for post {post.id}")
            media_object = create_media_object(post.image.url, post.caption)
            
            logger.info(f"Publishing media object {media_object['id']} for post {post.id}")
            success = publish_media_object(media_object['id'])
            
            if success:
                post.is_published = True
                post.save()
                logger.info(f"Successfully published post {post.id}")
            else:
                logger.error(f"Failed to publish post {post.id}")
        
        except Exception as e:
            logger.exception(f"Error publishing post {post.id}: {str(e)}")
