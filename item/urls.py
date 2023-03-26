from django.urls import path
from .import views


app_name='item'

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
    path('additem/',views.Addnewitem,name='additem'),
    path('<int:pk>/delete/',views.DeleteItem,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('',views.items,name='items')]

