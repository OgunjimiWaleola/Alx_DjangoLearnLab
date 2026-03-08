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