from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.sign_up,name='signup')
]
