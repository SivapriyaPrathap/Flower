from django.db import models

# Create your models here.
class Flower(models.Model):
    name=models.CharField(max_length=250)
    places = models.CharField(max_length=250)
    des=models.TextField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name



