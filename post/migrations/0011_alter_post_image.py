# Generated by Django 4.0.2 on 2022-05-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]