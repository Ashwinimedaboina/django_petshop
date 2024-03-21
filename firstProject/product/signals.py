from django.contrib.auth.signals import *

# user logged_in and user_logout

from django.contrib.auth.models import User

from django.dispatch import receiver


from django.db.models.signals import *
from .models import product


@receiver(user_logged_in,sender=User)
def log_in(sender,request,user,**kwargs):
    print("**************")
    print("logged in succesfully")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("arguments:",kwargs)
    print("**************")

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("$$$$$$$$$$$$$$")
    print("logged out succesfully")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("arguments:",kwargs)
    print("$$$$$$$$$$$$$$$$$")



@receiver(post_save,sender=product)
def productCreateSignal(sender,instance,**kwargs):
    print("***********product creatred*************")
    print("****************************************")
    print("sender:",sender)
    print("instance:",instance)
    print("arguments",kwargs)
    print("****************************************")


@receiver(post_delete,sender=product)
def productDeleteSignal(sender,instance,**kwargs):
    print("***********product deleted*************")
    print("****************************************")
    print("sender:",sender)
    print("instance:",instance)
    print("arguments",kwargs)
    print("****************************************")