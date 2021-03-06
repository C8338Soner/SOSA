# Generated by Django 4.0.2 on 2022-05-20 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_rename_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='post.Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(default=post.models.deleted_user, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='publisher', to=settings.AUTH_USER_MODEL),
        ),
    ]
