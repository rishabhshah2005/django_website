from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=300)
    time_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.search}'

class Product(models.Model):
    PRODUCT_TYPE = [
        ("G", "General"),
        ("VG", "Vegetables"),
        ("FT", "Fruits"),
        ('GR', "Groceries"),
        ("HG", "Hygiene"),
        ("GR", "Grooming"),
        ("CL", "Clothing")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length= 100)
    photo = models.FileField(blank=True, default='static/images/no_img.png')
    description = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=20, blank=True)
    primary_type = models.CharField(choices=PRODUCT_TYPE, max_length=2, default="G")

    def __str__(self):
        return f'{self.name}'
    
