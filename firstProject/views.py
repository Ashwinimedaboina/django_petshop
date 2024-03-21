from django.shortcuts import render
from product.models import product

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")   

def home(request):
    return render(request,"index.html") 


def search(request):
    query=request.GET.get('query','')
    #print(query)
    products=product.pm.all().filter(product_name__icontains=query)
    return render(request,"search.html",{"allproducts":products})        