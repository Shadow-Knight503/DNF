from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField as BaseCloudinaryField
from django.conf import settings


# Create your models here.
class CloudinaryField(BaseCloudinaryField):
    def upload_options(self, model_instance):
        return {
            'public_id': model_instance.name,
            'filename': Sale.Title,
            'unique_filename': False,
            'overwrite': False,
            'resource_type': 'auto',
            'tags': ['Sales'],
            'invalidate': True,
            'quality': 'auto:eco',
        }


class Company(models.Model):
    Name = models.CharField(max_length=200)
    Dscrp = models.TextField(max_length=500, default="Stuff")
    Logo = CloudinaryField('Logo')

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.Name


class Sale(models.Model):
    Title = models.CharField(max_length=200)
    Sale_Img = CloudinaryField('Sales')

    def __str__(self):
        return self.Title


class Product(models.Model):
    Comp = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=200)
    Price = models.CharField(max_length=10)
    Stock = models.IntegerField(default=10)
    Dscrp = models.TextField(max_length=500)

    def __str__(self):
        return self.Name


class ProdImg(models.Model):
    Prod = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    Img = CloudinaryField('Product Img')
    Sno = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.Prod.Name}-{self.Sno}"
