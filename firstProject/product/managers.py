from django.db import models

class productManager(models.Manager):

    def get_queryset(self):
        return productQuerySet(self.model)
                                                       
                                                       #return productQuerySet(self.model).getPawsIndia()          # return super().get_queryset().filter(product_price__gt=500) 
                                         # return super().get_queryset().order_by('product_name')-->it gives product in sorted order
 
                                    

    #def sorted(self):
        #return super().get_queryset().order_by('product_name') 

    def  sort_by_price(self):
        return super().get_queryset().order_by('product_price') 

class productQuerySet(models.QuerySet):
    def getPawsIndia(self):
        return self.filter(product_brand="Pawsup")

    def cat_products(self):
        return self.filter(product_name__icontains="cat") 

    def fruit_products(self):
        return self.filter(product_name__icontains="fruits")                                                                
 