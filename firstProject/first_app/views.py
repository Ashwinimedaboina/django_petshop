from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
def home(request):
    return HttpResponse("first view")

def firstpage(request):
    return HttpResponse("<h1>First Page</h1>")    

def about(request):
    return HttpResponse("<h1>about us</h1>")
def hello(request):
    return HttpResponse("<h1>hello world</h1>")
def bye(request):
    return HttpResponse("bye bye")
def goodMorning(request):
    return HttpResponse("hi good morning")  

def users(request):
    student={"id":101,"name":"nikita","age":18}
    return render(request,"about.html",student) 

def admin(request):
    student1={"s_id":1,"s_name":"navodhaya"}
    return render(request,"index.html",student1)

def register(request):
    return render(request,"register.html")

def submit(request):
    if request.method=="POST":              #in django it will store capital that's why it will write capital
        return render(request,"submit.html") #submit  is not equal to post method that's why it will go to get method
    if request.method=="GET":
        return render(request,"register.html")

#creating a class[class-based view] 

class firstView(View):
    def get(self,request):
        return HttpResponse("Class Based View-GET")
                        
class myView(View):
    name="nisha"
    def get(self,request):
        
        return render(request,"details.html",{"name":self.name})
