from django.contrib import admin
from .models import product_details,cartItem,Gallery,Billing,Order,OrderItem,UserEvent,ViewedProduct,Recommendation,Wishlist


admin.site.register(product_details)
admin.site.register(cartItem)
admin.site.register(Billing)

# Register your models here.


admin.site.register(Gallery)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserEvent)
admin.site.register(ViewedProduct)
admin.site.register(Recommendation)
admin.site.register(Wishlist)
