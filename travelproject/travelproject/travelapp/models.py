from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=350)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
def __str__(self):
    return self.name

class workers(models.Model):
    name=models.CharField(max_length=350)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()