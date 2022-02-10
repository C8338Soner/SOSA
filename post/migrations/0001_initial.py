# Generated by Django 4.0.2 on 2022-02-10 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=100000)),
                ('image', models.URLField(blank=True, max_length=10000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('1', 'Draft'), ('2', 'Published')], default=('1', 'Draft'), max_length=30)),
                ('likes', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(default='Deleted', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='userNpost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
