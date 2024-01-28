from django.db import models
class  Articles(models.Model):
    title=models.CharField(max_length=100)
    text_data= models.CharField(max_length=20000)
    

# Create your models here.
