# Generated by Django 4.0.3 on 2022-04-28 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pinterest',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website_url',
        ),
    ]
