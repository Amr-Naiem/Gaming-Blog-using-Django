# Generated by Django 4.0.3 on 2022-05-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_rename_post_image_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
