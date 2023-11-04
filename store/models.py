from django.db import models

# Create your models here.

#category
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250, blank=True)
    category_image = models.ImageField(upload_to = 'photos/catagories', blank=True)
    
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'catagories'


#Product details
class Product(models.Model):
    # id = models.AutoField(unique=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    created_date    = models.DateTimeField(auto_now_add=True)
    # created_date    = models.DateTimeField(auto_now_add=True, default= timezone.now)
    
    
    def __str__(self):
        return self.product_name