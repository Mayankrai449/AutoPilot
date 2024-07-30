import requests
from django.conf import settings

def create_media_object(image_url, caption):
    return make_api_request('me/media', method='POST', data={
        'image_url': image_url,
        'caption': caption,
    })

def publish_media_object(media_object_id):
    response = make_api_request(f"{media_object_id}/publish", method='POST')
    return 'id' in response

def make_api_request(endpoint, method='GET', params=None, data=None):
    url = f"https://graph.instagram.com/v12.0/{endpoint}"
    headers = {
        'Authorization': f'Bearer {settings.INSTAGRAM_ACCESS_TOKEN}',
    }
    
    response = requests.request(method, url, headers=headers, params=params, json=data)
    response.raise_for_status()
    return response.json()