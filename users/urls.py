from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('sign_up', views.signup, name='signup'),
]