# Social Media API

A Django REST API implementing user authentication for a social media platform.

## Features
- User Registration
- User Login
- Token Authentication
- User Profile Endpoint

## Setup

Clone repository

git clone https://github.com/yourusername/Alx_DjangoLearnLab.git

Install dependencies

pip install django djangorestframework

Run migrations

python manage.py migrate

Start server

python manage.py runserver

## API Endpoints

Register
POST /api/accounts/register/

Login
POST /api/accounts/login/

Profile
GET /api/accounts/profile/


## Posts Endpoints

GET /api/posts/  
List all posts

POST /api/posts/  
Create new post

GET /api/posts/{id}/  
Retrieve post

PUT /api/posts/{id}/  
Update post

DELETE /api/posts/{id}/  
Delete post


## Comments Endpoints

GET /api/comments/  
List comments

POST /api/comments/  
Create comment

GET /api/comments/{id}/  
Retrieve comment

PUT /api/comments/{id}/  
Update comment

DELETE /api/comments/{id}/  
Delete comment



## Follow System

Follow a user

POST /api/accounts/follow/{user_id}/

Unfollow a user

POST /api/accounts/unfollow/{user_id}/


## Feed Endpoint

Retrieve posts from users you follow

GET /api/feed/


## Likes Endpoints

POST /api/posts/<post_id>/like/ - Like a post
POST /api/posts/<post_id>/unlike/ - Unlike a post

## Notifications Endpoints

GET /api/notifications/ - Fetch your notifications