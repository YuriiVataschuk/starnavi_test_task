import json
import random
import requests

from api.models import Post


def bot_user_create_and_get_token():
    register_url = "http://127.0.0.1:8000/api/user/register/"
    user_data = {
        "username": f"user{str(random.randrange(0, 333, 1))}",
        "email": "user@user.com",
        "password": "asdf4321",
    }
    usr = requests.post(register_url, data=user_data)
    print(user_data)
    print("User registration response:", usr)

    if usr.status_code == 201:
        auth_url = "http://127.0.0.1:8000/api/user/token/"
        auth_data = {
            "username": user_data["username"],
            "password": user_data["password"],
        }
        auth_response = requests.post(auth_url, data=auth_data)
        if auth_response.status_code == 200:
            token = auth_response.json().get("access")
            return token
        else:
            print("Authentication failed.")
    else:
        print("User registration failed.")

    return None


def bot_post_create(token):
    post_url = "http://127.0.0.1:8000/api/api/posts/"
    postdata = {
        "content": "Hello world",
    }
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(post_url, data=postdata, headers=headers)
    print("Post creation response:", r)


def bot_post_like(token):
    posts = Post.objects.all()
    post_id = random.choice([i.id for i in posts])
    post_like_url = f"http://127.0.0.1:8000/api/api/posts/{post_id}/like/"
    headers = {"Authorization": "Bearer " + token}
    like = requests.post(post_like_url, headers=headers)
    print("like", like)


def main():
    with open(
        "api/bot_rules.json", "r"
    ) as read_file:
        bot = json.load(read_file)

    number_of_users = bot.get("number_of_users", 5)
    max_posts_per_user = bot.get("max_posts_per_user", 5)
    max_likes_per_user = bot.get("max_likes_per_user", 3)

    for _ in range(number_of_users):
        token = bot_user_create_and_get_token()
        if token:
            for _ in range(random.randint(1, max_posts_per_user)):
                bot_post_create(token)
            for _ in range(random.randint(1, max_likes_per_user)):
                bot_post_like(token)


if __name__ == "__main__":
    main()
