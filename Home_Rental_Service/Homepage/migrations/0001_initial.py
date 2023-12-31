# Generated by Django 4.0.4 on 2022-08-12 11:38

import datetime
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
                ('username', models.CharField(default='Username', max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('moment', models.DateTimeField(default=datetime.datetime.now)),
                ('images', models.ImageField(upload_to='post_images')),
            ],
        ),
        migrations.CreateModel(
            name='PostAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_div', models.CharField(max_length=20)),
                ('home_dist', models.CharField(max_length=20)),
                ('home_upa', models.CharField(max_length=20)),
                ('addr_desc', models.TextField(default=0, max_length=50)),
                ('contact1', models.EmailField(max_length=254)),
                ('contact2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=50)),
                ('room_no', models.IntegerField(default=0)),
                ('bedroom_no', models.IntegerField(default=0)),
                ('bathroom_no', models.IntegerField(default=0)),
                ('gas_facility', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Username', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('profileImg', models.ImageField(default='blankpp.png', upload_to='profile_imgs')),
                ('address', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
