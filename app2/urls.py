from django.urls import path
from . import views

urlpatterns=[
             path('',views.index,name='index'),
             path('ring/',views.ring,name='ring'),
             path('neck/',views.neck,name='neck'),
             path('ear/',views.ear,name='ear'),
             path('bracelet/',views.bracelet,name='bracelet'),
             path('image_list/',views.image_list,name='image_list'),
            path('about/',views.about,name='about'),
            path('contact/',views.contact,name='contact'),
            path('login/',views.login,name='login'),
            path('signup/',views.signup,name='signup'),
            path('logout/', views.logout, name='logout'),
            path('singlepr/<int:id>/',views.singleproduct,name='singleproduct'),
            path('image_list_1/',views.image_list_1,name='image_list_1'),
            path('cart/',views.cart,name='cart'),
            path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
             path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
            path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
            path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),  # Checkout page with cart + billing
        path('order_summary/', views.order_summary, name='order_summary'),
            path("payment-success/", views.payment_success, name="payment_success"),
                path("order-history/", views.order_history, name="order_history"),
                    path("recommendations/", views.recommendation_page, name="recommendations"),
                    path("product/<int:product_id>/", views.view_product, name="view_product"),
                        path("upload-outfit/", views.outfit_upload, name="upload_outfit"),






            ]
