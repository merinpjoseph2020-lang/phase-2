from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    msg=models.TextField()
    
    def __str__(self):
        return self.name
 

# class product_details(models.Model):
#     title=models.CharField(max_length=20)
#     description=models.TextField()
#     image=models.ImageField(upload_to='images/')
#     price=models.IntegerField()

#     def __str__(self):
#         return self.title

# class cartItem(models.Model):
#     product=models.ForeignKey(product_details,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)

#     @property
#     def total_price(self):
#         return self.product.price*self.quantity
#     def __str__(self):
#         return f"{self.quantity} of {self.product.title}"
class product_details(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()

    # Category needed for recommendations
    category = models.CharField(
        max_length=50,
        choices=[
            ("gold", "Gold"),
            ("silver", "Silver"),
            ("diamond", "Diamond"),
            ("traditional", "Traditional"),
            ("fashion", "Fashion"),
        ],
        default="fashion"
    )

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class cartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name} ({self.user.username})"

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
    
from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link billing to a user
    mobile = models.CharField(max_length=10, blank=False)
    alternate = models.CharField(max_length=10, blank=True, null=True)
    house = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    landmark = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mobile} - {self.city}"

from django.db import models
from django.contrib.auth.models import User
from .models import product_details


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        default="Processing"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.product_name
    


class UserEvent(models.Model):
    """Store user occasions: birthday, wedding, anniversary, etc."""
    EVENT_TYPES = [
        ("birthday", "Birthday"),
        ("anniversary", "Anniversary"),
        ("wedding", "Wedding"),
        ("festival", "Festival"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.event_type}"


class ViewedProduct(models.Model):
    """Track user browsing history for recommendations."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewed {self.product.title}"


class Recommendation(models.Model):
    """Store generated recommendations for a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)  # e.g., "Based on your wishlist"

    def __str__(self):
        return f"Recommendation for {self.user.username}: {self.product.title}"
from django.db import models
from django.contrib.auth.models import User



class OutfitUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outfit_image = models.ImageField(upload_to="outfits/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Outfit {self.id}"


class OutfitRecommendation(models.Model):
    outfit = models.ForeignKey(OutfitUpload, on_delete=models.CASCADE, related_name="recommendations")
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product.title} for Outfit {self.outfit.id}"
