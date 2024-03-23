from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Budget(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    earnings= models.IntegerField(default=0)
    name= models.CharField(max_length=150, default='something')
    price= models.IntegerField(default=0)
