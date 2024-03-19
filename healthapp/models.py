from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class Services(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    
    # class Post(TimeStamped):
    # user = models.ForeignKey(User)
    # photo = models.ImageField(upload_to='upload/')
    # hidden = models.BooleanField(default=False)
    # upvotes = models.PositiveIntegerField(default=0)
    # downvotes = models.PositiveIntegerField(default=0)
    # comments = models.PositiveIntegerField(default=0)