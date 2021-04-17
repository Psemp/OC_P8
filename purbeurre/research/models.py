from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)  # ???
    translated_name = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    login = models.CharField(max_length=200, unique=True)
    pwd_hash = models.CharField(max_length=1000, unique=False)
    is_admin = models.BooleanField(default=False)
    created_time = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=False)
    brand = models.CharField(max_length=200, unique=False)
    url = models.URLField(unique=True)
    picture_url = models.URLField(unique=True)
    product_categories = models.ManyToManyField(Category, related_name='product_categories', blank=True)
    favorites = models.ManyToManyField(Account, related_name='favorites', blank=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100, unique=False)
    location = models.CharField(max_length=200, unique=False)
    product_availability = models.ManyToManyField(Product, related_name='store_availability', blank=True)

    def __str__(self):
        return self.name
