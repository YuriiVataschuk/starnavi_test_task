## Description

This project is a social media analytics platform with key features including user registration, post creation, post liking, and user activity tracking. The system is powered by Django and uses token authentication (preferably JWT) for user access control. Users can sign up, create posts, like and unlike posts, and view analytics on the number of likes made during a specified date range. Additionally, the platform keeps track of user activity by recording login and request times. An automated bot is used to simulate user interactions based on a configuration file, including user signups, posting, and liking posts.

## Instalation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py start_bot

## Endpoints

api/api/posts/ (GET) - get all posts
/api/apiposts/id_number/ (GET) - get a single post by id
/api/api/posts/id_number/like (POST) - like or unlike a post by id
/api/api/posts/ (POST) - create a new post
/api/user/register/ (POST) - registration endpoint
/api/user/token/ (POST) - authentication for get token by username and password
/api/user/token/refresh/ - refresh token
/api/user/token/verify/ - verify token
/api/analytics/?date_from=2021-02-02&date_to=2021-11-10 (GET) - analytics about how many likes was made. API return analytics aggregated by day. date_from is required parameter.
/api/ analitic/users/ - analytics about users last requests and last logins
