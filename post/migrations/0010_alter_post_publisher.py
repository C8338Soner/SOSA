# Generated by Django 4.0.2 on 2022-05-19 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0009_alter_post_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(default=post.models.deleted_user, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='post_publisher', to=settings.AUTH_USER_MODEL),
        ),
    ]