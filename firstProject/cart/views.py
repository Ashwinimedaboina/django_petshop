
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,HttpResponse
from product.models import product
from .models import Cart,CartItem
# Create your views here.

def add_to_cart(request,productID):
    products=get_object_or_404(product,id=productID)
    print(products.product_name)

    currentUser=request.user

    Carts,created=Cart.objects.get_or_create(user=currentUser)

    print(created)

    item,item_created=CartItem.objects.get_or_create(Cart=Carts,products=products)

    quantity=request.GET.get("quantity")

    if not item_created:
        item.quantity+=int(quantity)
    else:
        item.quantity=1 

    item.save()    

    return HttpResponseRedirect("/p/productlookup/")

#==========================================================================================
   #view cart
#==========================================================================================

def view_cart(request):
    currentUser=request.user
    Carts,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=Carts.cartitem_set.all()
    print(cartItems)
    finalAmount=0
    for i in cartItems:
        finalAmount+=i.quantity*i.products.product_price
    return render(request,"cart.html",{"items":cartItems,"finalAmount":finalAmount})
#======================================================================
#                           update cart 
#======================================================================

def update_cart(request,CartItemId):
    cartItem=get_object_or_404(CartItem,pk=CartItemId)
    quantity=request.GET.get("quantity")
    cartItem.quantity=int(quantity)
    cartItem.save()

    return HttpResponseRedirect("/cart/")

#==========================================================================
#              delete cart_item
#==============================================================================
def delete_cart(request,CartItemId):
    cartItem=get_object_or_404(CartItem,pk=CartItemId)
    cartItem.delete()
    return HttpResponseRedirect("/cart/")

#=============================================================================== 
#                      checkout function   
#==================================================================
from .forms import OrderForm
from .models import Order,orderItem
import uuid
def check_out(request):
    currentUser=request.user
    initial={
        "user":currentUser,
        "firstName":currentUser.get_short_name(),
        "lastName":currentUser.last_name,
        "email":currentUser.email




    }
    form=OrderForm(initial=initial)
    currentUser=request.user
    Carts,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=Carts.cartitem_set.all()
    print(cartItems)
    finalAmount=0
    for i in cartItems:
        finalAmount+=i.quantity*i.products.product_price
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            user=request.user
            firstName=form.cleaned_data['firstName']
            lastName=form.cleaned_data['lastName']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phoneNo=form.cleaned_data['phoneNo']
            email=form.cleaned_data['email']

            order_id=str(uuid.uuid4())

            order=Order.objects.create(user=user,
            firstName=firstName,
            lastName=lastName,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            phoneNo=phoneNo,
            email=email,
            order_id=order_id[0:8] )  

            for item in cartItems:
                  orderItem.objects.create(
                  order=order,
                  products=item.products,
                 quantity=item.quantity,
                 total=item.quantity*item.products.product_price
        )


            

        return HttpResponseRedirect("/payment/"+order_id[0:8])
    return render(request,"checkout.html",{"form":form,"items":cartItems,"finalAmount":finalAmount})


#=======================================================
#    make payment
#=========================================================
import razorpay

def make_payment(request,order_id):
    #print(order_id)
    order=Order.objects.get(pk=order_id)  #Order is class name
    orderItems=order.orderitem_set.all()   #order.orderItem is in models.py

    amount=0
    for i in orderItems:
        amount+=i.total

    print(amount) 
    
    client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))

    data = { "amount": amount*100, "currency": "INR", "receipt": order_id,"payment_capture":1 }
    payment = client.order.create(data=data)   


    return render(request,"payment.html",{"payment":payment})
#=======================================================================
#success
#=====================================================================================================    

from django.views.decorators.csrf import csrf_exempt    
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

@csrf_exempt
def success(request,order_id):
    if request.method=="POST":
        client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))
        check=client.utility.verify_payment_signature({
   'razorpay_order_id': request.POST.get("razorpay_order_id"),
   'razorpay_payment_id': request.POST.get("razorpay_payment_id"),
   'razorpay_signature': request.POST.get("razorpay_signature")})
        if check:
            order=Order.objects.get(pk=order_id)
            order.paid=True
            order.save()
            cart=Cart.objects.get(user=request.user)
            orderItems=order.orderitem_set.all()
            send_mail(
                "order placed..",#subject
                "",#message
                settings.EMAIL_HOST_USER,
                ["priyanka.vibhute@itvedant.com","jari.jafri21@gmail.com"],
                fail_silently=False,
                html_message=render_to_string("email.html",{"items":orderItems}))
            cart.delete()
            
            return render(request,"success.html",{})    