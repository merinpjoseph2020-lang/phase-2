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
        return redirect('image_list')


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
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
# from .models import cartItem, product_details
# @login_required(login_url='login')
# def cart(request):
#     cart_items = cartItem.objects.all()

#     subtotal = sum(item.product.price * item.quantity for item in cart_items)
#     shipping = 10 if subtotal > 0 else 0
#     total = subtotal + shipping

#     return render(request, "cart.html", {
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#         'shipping': shipping,
#         'total': total,
#     })
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import cartItem

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import cartItem

@login_required(login_url='login')
def cart(request):
    # Fetch only cart items for the logged-in user
    cart_items = cartItem.objects.filter(user=request.user)

    # Calculate subtotal
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    
    # Shipping logic (example)
    shipping = 10 if subtotal > 0 else 0
    total = subtotal + shipping

    return render(request, "cart.html", {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import cartItem, product_details

@login_required(login_url='login')
def cart(request):
    cart_items = cartItem.objects.filter(user=request.user)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = 10 if subtotal > 0 else 0
    total = subtotal + shipping

    return render(request, "cart.html", {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })


@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(product_details, id=product_id)

    # Get or create cart item for this user
    cart_item, created = cartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required(login_url='login')
def update_cart(request, item_id):
    item = get_object_or_404(cartItem, id=item_id, user=request.user)
    if request.method == "POST":
        item.quantity = int(request.POST.get("quantity"))
        item.save()
    return redirect('cart')


@login_required(login_url='login')
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(cartItem, id=item_id, user=request.user)
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
from django.shortcuts import render, redirect
from .forms import DeliveryDetailsForm
from .models import cartItem  # Assuming CartItem exists
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import DeliveryDetailsForm
# from shop.models import cartItem  # Adjust if needed

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay

from .models import cartItem, Billing, Order, OrderItem
from .forms import DeliveryDetailsForm

# ------------------------ Checkout ------------------------ #
@login_required(login_url='login')
def checkout(request):
    # Fetch only cart items for the logged-in user
    cart_items = cartItem.objects.filter(user=request.user)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = 10 if subtotal > 0 else 0
    total_price = subtotal + shipping

    if request.method == 'POST':
        form = DeliveryDetailsForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user  # Associate with logged-in user
            delivery.save()

            # Create an Order
            order = Order.objects.create(user=request.user, total_amount=total_price)

            # Create Order Items
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Clear the user's cart
            

            return redirect('order_summary')
    else:
        form = DeliveryDetailsForm()

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total_price': total_price,
        'form': form
    }
    return render(request, 'checkout.html', context)


# ------------------------ Order Summary ------------------------ #
@login_required(login_url='login')
def order_summary(request):
    cart_items = cartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty. Add items before checkout.")
        return redirect('cart')

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if total_price <= 0:
        messages.error(request, "Invalid order amount.")
        return redirect('cart')

    delivery = Billing.objects.filter(user=request.user).last()

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    amount = int(total_price * 100)  # Amount in paise

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, "order_summary.html", {
        "cart_items": cart_items,
        "total_price": total_price,
        "delivery": delivery,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "razorpay_order_id": order["id"],
        "amount": amount
    })


# ------------------------ Payment Success ------------------------ #
@login_required(login_url='login')
def payment_success(request):
    # Clear only the logged-in user's cart
    cart_items = cartItem.objects.filter(user=request.user)
    cart_items.delete()
    return render(request, "payment_success.html")


# ------------------------ Order History ------------------------ #
@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, "order_history.html", {'orders': orders})
def generate_recommendations(user):
    recommended = []

    # 1. Based on events
    events = UserEvent.objects.filter(user=user)
    for e in events:
        if e.event_type == "birthday":
            recommended += product_details.objects.filter(title__icontains="gift")
        elif e.event_type == "anniversary":
            recommended += product_details.objects.filter(title__icontains="ring")
        elif e.event_type == "wedding":
            recommended += product_details.objects.filter(price__gte=2000)

    # 2. Based on wishlist similarity
    wishlist_items = Wishlist.objects.filter(user=user).values_list("product", flat=True)
    if wishlist_items:
        recommended += product_details.objects.exclude(id__in=wishlist_items)[:5]

    # 3. Based on browsing history
    viewed = ViewedProduct.objects.filter(user=user).values_list("product", flat=True)
    if viewed:
        recommended += product_details.objects.exclude(id__in=viewed)[:5]

    # Remove duplicates
    seen = set()
    final_list = []
    for r in recommended:
        if r.id not in seen:
            final_list.append(r)
            seen.add(r.id)

    return final_list[:10]
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Import models
from .models import (
    UserEvent,
    ViewedProduct,
    Wishlist,
    Recommendation,
    OrderItem,
)

# Import your custom recommendation generator
# from .recommendations import generate_recommendations



@login_required
def recommendation_page(request):
    user = request.user

    # Generate recommended product list
    products = generate_recommendations(user)

    # Clear old recommendations and store new ones
    Recommendation.objects.filter(user=user).delete()
    for p in products:
        Recommendation.objects.create(
            user=user,
            product=p,
            reason="Personalized suggestion based on your activity"
        )

    # Identify which data sources influenced recommendations
    reasons = []

    if UserEvent.objects.filter(user=user).exists():
        reasons.append("✔ Based on your upcoming events (Birthday, Anniversary, Wedding).")

    if Wishlist.objects.filter(user=user).exists():
        reasons.append("✔ Based on items from your wishlist.")

    if ViewedProduct.objects.filter(user=user).exists():
        reasons.append("✔ Based on products you viewed recently.")

    if OrderItem.objects.filter(order__user=user).exists():
        reasons.append("✔ Based on your previous purchases.")

    if not reasons:
        reasons.append("✔ Smart suggestions tailored for you.")

    return render(request, "recommendations.html", {
        "products": products,
        "reasons": reasons
    })
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product_details, ViewedProduct

@login_required
def view_product(request, product_id):
    # Get the product
    product = get_object_or_404(product_details, id=product_id)

    # Save viewed product entry for recommendations
    ViewedProduct.objects.create(
        user=request.user,
        product=product
    )

    return render(request, "view_product.html", {"product": product})



# ---------------- OUTFIT COLOR SYSTEM --------------------

import cv2
import numpy as np
from sklearn.cluster import KMeans
from .models import product_details


def extract_dominant_color(image_path, k=3):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img)

    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    label_counts = np.bincount(labels)

    # Pick the most common cluster → TRUE dominant color
    dominant_color = colors[label_counts.argmax()]

    return tuple(dominant_color)


def map_color_to_style(rgb):
    r, g, b = rgb

    if r > 150 and g < 130:
        return "gold"

    if b > 120 and r < 150:
        return "silver"

    if r > 180 and g > 180 and b > 180:
        return "diamond"

    return "generic"


def recommend_ornaments(image_path):
    dominant_color = extract_dominant_color(image_path)
    style = map_color_to_style(dominant_color)

    if style == "gold":
        return product_details.objects.filter(
            category__icontains="gold"
        ).order_by("?")[:10]

    if style == "silver":
        return product_details.objects.filter(
            category__icontains="silver"
        ).order_by("?")[:10]

    if style == "diamond":
        return product_details.objects.filter(
            category__icontains="diamond"
        ).order_by("?")[:10]

    # generic fallback
    return product_details.objects.all().order_by("?")[:10]


# ---------------- UPLOAD VIEW --------------------

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required
def outfit_upload(request):
    recommended_products = None

    if request.method == "POST" and request.FILES.get("outfit"):
        outfit_image = request.FILES["outfit"]

        fs = FileSystemStorage(location="media/outfits/")
        filename = fs.save(outfit_image.name, outfit_image)
        image_path = fs.path(filename)

        recommended_products = recommend_ornaments(image_path)

    return render(request, "outfit_recommendation.html", {
        "products": recommended_products,
    })
