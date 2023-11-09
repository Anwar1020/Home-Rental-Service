from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from tokenize import Triple
from urllib import request
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


# class NewCommonModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, default= 'Username', null=False)
    email = models.EmailField()
    profileImg = models.ImageField(upload_to='profile_imgs', default ='blankpp.png')
    address = models.TextField(max_length= 100)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    username = models.CharField(max_length=20, default= 'Username', null=False)
    price = models.IntegerField(default=0)
    moment = models.DateTimeField(default=datetime.now)
    images = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.username

class PostDetail(models.Model):
    house_name = models.CharField(max_length=50)
    room_no = models.IntegerField(default=0)
    bedroom_no = models.IntegerField(default=0)
    bathroom_no = models.IntegerField(default=0)
    gas_facility = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.house_name

class PostAddress(models.Model):
    home_div = models.CharField(max_length=20)
    home_dist = models.CharField(max_length=20)
    home_upa = models.CharField(max_length=20)
    addr_desc = models.TextField(max_length=50, default=NULL)
    contact1 = models.EmailField()
    contact2 = models.IntegerField()