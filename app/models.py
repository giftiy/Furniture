from django.db import models

class Product(models.Model):
    # Define the category choices
    CATEGORY_CHOICES = [
        ('sofa', 'Sofa'),
        ('recliner', 'Recliner'),
        ('nightstand', 'Nightstand'),
        ('dresser', 'Dresser'),
        ('dining', 'Dining Table'),
        ('desk', 'Desk'),
        ('coffee_table', 'Coffee Table'),
        ('bed', 'Bed'),
        ('armchair', 'Armchair'),
    ]

    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()  # Changed to FloatField for consistency
    composition = models.TextField(default="")
    prodapp = models.CharField(max_length=100, default="")  # Added max_length
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Corrected choices
    product_image = models.ImageField(upload_to="product")

    def __str__(self):
        return self.title