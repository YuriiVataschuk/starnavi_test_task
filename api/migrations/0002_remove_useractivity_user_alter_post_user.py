# Generated by Django 4.2.6 on 2023-10-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useractivity",
            name="user",
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.CharField(max_length=255),
        ),
    ]