from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Book(models.Model):
    x = [
        ('available','available'),
        ('rental','rental'),
        ('solid','solid'),
    ]

    title = models.CharField(max_length=70)
    auther = models.CharField(max_length=70)
    book_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    auther_photo =  models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    price_day_rent = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    period_rent = models.IntegerField(null=True, blank=True)
    total_rental =models.DecimalField(max_digits=7,decimal_places=5, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    status = models.CharField(max_length=90, choices=x, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.title