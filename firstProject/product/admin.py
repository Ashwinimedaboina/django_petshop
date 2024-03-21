from django.contrib import admin
from  .models import product,Category
# Register your models here.


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_price','product_brand','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')
#admin.site.register(product,productAdmin)

