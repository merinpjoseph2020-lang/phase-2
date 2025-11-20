from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    msg=models.TextField()
    
    def __str__(self):
        return self.name
 

class product_details(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    price=models.IntegerField()

    def __str__(self):
        return self.title

class cartItem(models.Model):
    product=models.ForeignKey(product_details,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price*self.quantity
    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

from django.db import models
from django.contrib.auth.models import User
# from .models import product_details   # change to your actual product model

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')  # prevents duplicate wishlist items

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
class Gallery(models.Model):
    product = models.ForeignKey(
        product_details,
        related_name="gallery",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"{self.product.title} - Gallery Image"