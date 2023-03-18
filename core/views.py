from django.shortcuts import render
from item.models import Item,Category
from .forms import SignupForm


# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{'items':items,'categories':categories})

def contact(request):
    return render(request,"core/contact.html")

def sign_up(request):
    form=SignupForm()
    if request.method==['POST']:
        pass
    return render(request,'core/sign_up.html',{'form':form})
        
