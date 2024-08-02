from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

class Product(models.Model):
    product_name = models.CharField(null=False, blank=False, max_length=50)
    product_image = models.ImageField(null=False, upload_to='product')
    product_price = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_no = models.IntegerField()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Cart_items(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
