# Generated by Django 4.0.2 on 2022-03-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default=('1', 'Draft'), max_length=30),
        ),
    ]
