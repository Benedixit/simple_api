from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    product_detail = models.TextField()
    specifications = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Reviews(models.Model):
    review_text = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id

class Seller(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, default=None)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        return self.name