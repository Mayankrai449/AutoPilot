# AutoPilot
# Social Media Automation App

## Overview

This Social Media Automation App is a comprehensive platform leveraging the Instagram Graph API to enable users to schedule post uploads, automate comment replies, and manage direct message responses. It provides Instagram user data analytics and utilizes AWS S3 for image storage.

## Features

- Post scheduling
- Automated comment replies
- Direct message management
- Instagram user data analytics
- Image storage using AWS S3

## Tech Stack

- Backend: Python, Django
- Database: PostgreSQL
- Task Queue: Celery
- Cloud Storage: AWS S3
- API: Instagram Graph API

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Mayankrai449/AutoPilot.git
   cd AutoPilot
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your environment variables (see Environment Variables section below)

6. Run database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file in the root directory and add the following variables:

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
AWS_S3_REGION_NAME=your_s3_region

INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
```
## Future Plans

I aim to expand this project into a comprehensive social media automation service tailored for business accounts. This service will provide advanced tools to help businesses manage their social media presence with ease and efficiency.

Contact: mayankraivns@gmail.com