from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models


type=(
    ('electronics','electronics'),
    ('vehicles','vehicles'),
    ('furniture','furniture'),
    ('houses','house')
    )

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)   
    name = models.CharField(max_length=100)# For the name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    image = models.ImageField(upload_to='images/')  # Image field for uploading images
    address = models.CharField(max_length=255)
    contact_no=models.IntegerField(max_length=10)
    type=models.CharField(choices=type,max_length=20)
      # Address or location related to the product

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    myid=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class delivery(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=255)
    mobile=models.IntegerField(max_length=100)
    payment=models.CharField(max_length=100)
    orderid=models.ForeignKey(Product,on_delete=models.CASCADE)
    



