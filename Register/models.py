
from django.db import models
class Register(models.Model):
    S_No = models.IntegerField()
    Name = models.CharField(max_length=50)
    Contact_No = models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    