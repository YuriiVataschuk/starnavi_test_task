from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import datetime


@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    user.last_login = datetime.datetime.now()
    user.save()
