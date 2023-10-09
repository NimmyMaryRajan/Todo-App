from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('new_task', views.new_task, name='new'),
    path('details/<str:taskid>', views.details, name='detail'),
    path('delete/<str:taskid>', views.delete_task, name='delete'),
    ]