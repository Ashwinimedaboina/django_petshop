from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from.models import product,Category

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required(login_url="/login/"),name="dispatch")
class product_view(ListView):
    model=product
    template_name="products.html"

class product_detail_view(DetailView):
    model=product
    template_name="product_detail.html"
    context_object_name="p"

def field_lookup(request):
        products=product.cm.all()
        #products=product.cm.all().getPawsIndia
        #products=product.cm.all().cat_products()
       # products=product.cm.all().filter(Q(id=1)&Q (product_name="fruits"))
        #products=product.cm.all().filter(Q(product_price__lt="1200")& Q (product_name__icontains="fruits"))
        #products=product.cm.all().filter(Q(product_price__lt="1000")|Q (product_brand__icontains="fruits"))
        #products=product.cm.all().filter(~Q(product_name="fruits"))
        #products=product.objects.filter(product_brand="pawsup")
        #products=product.objects.filter(product_name="fruits")
        #products=product.object.filter(product_price__Lt="600")
        #products=product.object.filter(product_price__lte="600")
        #products=product.object.filter(product_name__contains="fruits")
        #products=product.object.filter(product_name__icontains="Fruits")
        #products=product.object.filter(product_name__startswith="p")
        #products=product.object.filter(product_name__endswith="s")
        #products=product.object.filter(product_id__in=[5,6,7])
        return render(request,"productlookup.html",{"product":products})


class CategoryDetailView(DetailView):
    model=Category
    template_name="category.html"
    context_object_name="category"
    slug_field="slug"

