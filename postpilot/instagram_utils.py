import requests
from django.conf import settings
from typing import Optional, Dict, Any
import logging
import json

logger = logging.getLogger(__name__)

API_VERSION = "v20.0"
BASE_URL = f"https://graph.instagram.com/{API_VERSION}"

def create_media_object(image_url: str, caption: str) -> Optional[Dict[str, Any]]:
    # First, check if the image is accessible
    if not is_image_accessible(image_url):
        logger.error(f"Image at {image_url} is not accessible")
        return None

    return make_api_request('me/media', method='POST', data={
        'image_url': image_url,
        'caption': caption,
        'access_token': settings.INSTAGRAM_ACCESS_TOKEN,
    })

def is_image_accessible(url: str) -> bool:
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200 and response.headers.get('Content-Type', '').startswith('')
    except requests.RequestException:
        return False

def publish_media_object(media_object_id: str) -> bool:
    response = make_api_request(f"{media_object_id}/publish", method='POST')
    return bool(response and 'id' in response)

def make_api_request(endpoint: str, method: str = 'GET', params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        'Content-Type': 'application/json',
    }
    
    if method == 'GET':
        params = params or {}
        params['access_token'] = settings.INSTAGRAM_ACCESS_TOKEN
    else:
        data = data or {}
        data['access_token'] = settings.INSTAGRAM_ACCESS_TOKEN

    try:
        response = requests.request(method, url, headers=headers, params=params, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")
        if hasattr(req_err, 'response') and req_err.response is not None:
            logger.error(f"Response content: {req_err.response.content}")
            try:
                error_detail = json.loads(req_err.response.content)
                logger.error(f"Error detail: {error_detail.get('error', {}).get('message', 'No detailed message')}")
            except json.JSONDecodeError:
                logger.error("Could not parse error response as JSON")
    except ValueError as json_err:
        logger.error(f"JSON decoding error: {json_err}")
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
    return None
