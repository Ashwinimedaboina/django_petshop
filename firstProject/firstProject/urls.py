"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from first_app import views

from django.conf.urls.static import static
from firstProject import settings
from .views import about,register,user_login,user_logout
from .views import contact,home,search
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('',views.firstpage,name="homepage"),
    path('about_us',views.about),
    path('hello',views.hello),
    path('bye',views.bye),
    path('goodMorning',views.goodMorning),
    path('users',views.users),
    path('admins',views.admin),
    #path('register',views.register),
    path('submit',views.submit),
    path("class",views.firstView.as_view()),
    path("details",views.myView.as_view(name="nithya")),
    path("p/",include('product.urls')),
    path("about/",about),
    path("contact/",contact),
    path("",home),
    path("search/",search),
    path("register/",register),
    path("login/",user_login),
    path("logout/",user_logout,name="logout"),
    path("",include("cart.urls"))
   
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)