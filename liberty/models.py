from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from liberty.utils import avatar_path, image_path

    
# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length= 28)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    avatar = models.ImageField(upload_to= avatar_path, default ='avatar.jpg' )
    like_count = models.IntegerField(default=0)

    def str(self) -> str:
        return self.first_name


class Item(models.Model):
    image = models.ImageField(upload_to=image_path, default ='Image.jpg')
    title = models.CharField(max_length = 128)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'items' )
    body = models.TextField()
    bid = models.FloatField()
    owner = models.CharField(max_length = 28)
    owner_username = models.CharField(max_length = 28)
    ends_in = models.TimeField()
    category =  models.ForeignKey("Category", on_delete = models.CASCADE, related_name='items')

class Category(models.Model):
    name = models.CharField(max_length=128,  null=False, blank=False)

    def __str__(self) -> str:
        return self.name