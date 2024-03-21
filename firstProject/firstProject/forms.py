from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        #fields="__all__"  #we wnt to see all information in form we use these one
        fields=["username","email","first_name","last_name"]
        labels={"username":"Enter Username","email":"Enter Email","first_name":"Enter FirstName","last_name":"Enter LastName"}