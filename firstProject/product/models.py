from django.db import models
from .managers import productManager
from autoslug import AutoSlugField

# Create your models here.
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=12)
    slug=AutoSlugField(populate_from="category_name")


    def __str__(self):
        return self.category_name

class product(models.Model):
    product_name=models.CharField(max_length=100,default="productName")
    product_description=models.TextField(default="description")
    product_price=models.IntegerField(default=0)
    product_brand=models.CharField(max_length=75,default="Paws")
    product_picture=models.ImageField(upload_to="images/",default="")
    #category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)#cascade it will delete  all base products also
    #category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)#it will  not allows to delete and protect it
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)#it allows to delete it deletes only the slug in product table
    
    pm=models.Manager()  #model manager name
    cm=productManager()  #custom manager

    def __str__(self):
    
        return self.product_name
    