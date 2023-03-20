from django.shortcuts import render,redirect
from item.models import Item,Category,User
from .forms import SignupForm,LoginForm


# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{'items':items,'categories':categories})

def contact(request):
    return render(request,"core/contact.html")

def sign_up(request):
    
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form=SignupForm()

    return render(request,'core/sign_up.html',{'form':form})
        
def log_in(request):
   pass
# log in view created at urls.py  