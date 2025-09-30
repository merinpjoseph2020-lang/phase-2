from django.urls import path
from . import views

urlpatterns=[
             path('',views.index,name='index'),
             path('ring/',views.ring,name='ring'),
             path('neck/',views.neck,name='neck'),
             path('ear/',views.ear,name='ear'), path('product/',views.product,name='product'),
             path('bracelet/',views.bracelet,name='bracelet'),
             path('products/',views.products,name='products'),
            path('about/',views.about,name='about'),
            path('contact/',views.contact,name='contact'),]
