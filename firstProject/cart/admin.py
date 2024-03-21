from django.contrib import admin
from .models import Order,orderItem

# Register your models here.
class orderItemInline(admin.TabularInline):
    model=orderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[orderItemInline] 


admin.site.register(Order,OrderAdmin)
admin.site.register(orderItem)


