from django.contrib import admin
from .models import Sale, Product, ProdImg, Company

# Register your models here.
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(ProdImg)
admin.site.register(Company)
