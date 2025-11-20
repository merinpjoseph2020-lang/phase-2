from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import contact_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def mypage(request):
    return HttpResponse("heloooooo")

def mypage1(request):
    return render(request,"demo.html")
def index(request):
    return render(request,"index.html")
def ring(request):
    return render(request,"ring.html")
def neck(request):
    return render(request,"neck.html")
def ear(request):
    return render(request,"ear.html")
# def products(request):
#     return render(request,"products.html")
# def product(request):
#     return render(request,"product.html")
def bracelet(request):
    return render(request,"bracelet.html")
def contact(request):
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form=contact_form()
    return render(request,'contact.html',{ "form":form})
    
    
        
    return render(request,"contact.html")

def signup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        passwd=request.POST['passwd']
        if User.objects.filter(username=fullname).exists():
            messages.error(request,"username already exists")
        if User.objects.filter(email=email).exists():
            messages.error(request,"username already exists")
        user=User.objects.create_user(username=fullname,email=email,password=passwd)
        user.save()
        messages.success(request,"Registration successfull")
        return redirect('products')


    return render(request,"signup.html")


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Convert email to username (since Django's default authenticate uses username)
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username  # get the corresponding username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome back to Leonora Jewels!")
            return redirect('image_list')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, "login.html")

    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')


def about(request):
    return render(request,"about.html")

from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # redirect to your login page
from .models import product_details,cartItem
def image_list(request):
    images=product_details.objects.all()
    return render(request,'products.html',{'images' :images})
def image_list_1(request):
    images=product_details.objects.all()
    return render(request,'neck.html',{'images' :images})

def singleproduct(request,id):
    image=get_object_or_404(product_details,id=id)
    return render(request,"product.html",{"image":image})

from django.shortcuts import render, redirect, get_object_or_404
from .models import cartItem, product_details

from django.shortcuts import render, redirect, get_object_or_404
from .models import cartItem, product_details

def cart(request):
    cart_items = cartItem.objects.all()

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = 10 if subtotal > 0 else 0
    total = subtotal + shipping

    return render(request, "cart.html", {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(product_details, id=product_id)

    cart_item, created = cartItem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def update_cart(request, item_id):
    item = get_object_or_404(cartItem, id=item_id)
    if request.method == "POST":
        item.quantity = int(request.POST.get("quantity"))
        item.save()
    return redirect('cart')


def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(cartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist, product_details

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(product_details, id=product_id)

    # Prevent duplicates
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        messages.success(request, "Added to wishlist ❤️")
    else:
        messages.info(request, "Already in wishlist!")

    return redirect('wishlist')
@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "wishlist.html", {"items": items})
@login_required
def remove_from_wishlist(request, product_id):
    item = get_object_or_404(Wishlist, user=request.user, product_id=product_id)
    item.delete()
    messages.success(request, "Removed from wishlist ❌")
    return redirect('wishlist')


from django.shortcuts import render

from django.db.models import Q

def search(request):
    query = request.GET.get('q', '')

    products = product_details.objects.filter(
        Q(title__icontains=query) |
        Q(price__icontains=query) 
       
    ) if query else []

    return render(request, 'search.html', {'products': products})
