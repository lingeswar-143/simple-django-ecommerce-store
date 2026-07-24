from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
        ('Accessory', 'Accessory'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Mobile'
    )

    featured = models.BooleanField(default=False)

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5
    )

    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name