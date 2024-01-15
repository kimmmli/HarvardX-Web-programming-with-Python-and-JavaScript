from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auctionlist(models.Model):
    auc_name=models.CharField(max_length=64)
    auc_descrip=models.CharField(max_length=640)
    auc_pic=models.