# Generated by Django 4.2.6 on 2023-10-13 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0004_alter_post_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserActivity",
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]