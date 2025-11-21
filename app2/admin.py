from django.contrib import admin
from .models import product_details,cartItem,Gallery,Billing


admin.site.register(product_details)
admin.site.register(cartItem)
admin.site.register(Billing)

# Register your models here.


admin.site.register(Gallery)