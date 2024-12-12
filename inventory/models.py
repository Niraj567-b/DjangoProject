from django.db import models

# Create your models here.

class Inventory(models.Model):
    itemName = models.TextField(max_length=125, null = False)
    itemCount = models.IntegerField(null = False)
    Expires_on = models.DateField(null = False)
    Description = models.TextField(max_length=500)




