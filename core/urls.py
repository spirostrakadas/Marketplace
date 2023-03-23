from django.urls import path
from .views import index
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.sign_up,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    #login redirect defined in settings.py LOGIN_REDIRECT_URL='/'
]
