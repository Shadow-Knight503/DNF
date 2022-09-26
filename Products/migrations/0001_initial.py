# Generated by Django 4.1.1 on 2022-09-26 08:34

import Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Sale_Img', Products.models.CloudinaryField(max_length=255, verbose_name='Sales')),
            ],
        ),
    ]