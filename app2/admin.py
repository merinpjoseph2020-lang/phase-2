from django.contrib import admin
from .models import product_details,cartItem,Gallery


admin.site.register(product_details)
admin.site.register(cartItem)

# Register your models here.


admin.site.register(Gallery)