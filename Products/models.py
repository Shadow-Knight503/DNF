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


class Sale(models.Model):
    Title = models.CharField(max_length=200)
    Sale_Img = CloudinaryField('Sales', resource_type="auto")

    def __str__(self):
        return self.Title
