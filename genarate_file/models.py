from django.db import models


# Create your models here.
class FileCSVModel(models.Model):
    file = models.FileField(upload_to='data/', max_length=254)
    filename = models.CharField(max_length=254)
