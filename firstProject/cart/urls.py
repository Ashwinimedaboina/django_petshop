from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("add-to-cart/<int:productID>",views.add_to_cart,name="addtocart"),
    path("cart/",views.view_cart,name="viewcart"),
    path("cart/update/<int:CartItemId>/",views.update_cart,name="updatecart"),
    path("cart/delete/<int:CartItemId>",views.delete_cart,name="deleteCartItem"),
    path("checkout/",views.check_out,name="checkout"),
    path("payment/<str:order_id>",views.make_payment,name="payment"),
    path("success/<str:order_id>",views.success,name="success")
    ]