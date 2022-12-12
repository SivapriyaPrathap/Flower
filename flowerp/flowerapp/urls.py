from . import views
from django.contrib import admin
from django.urls import path
app_name='flowerapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('detail/<int:id>/',views.detail,name="detail"),
    path('update/<int:id>/',views.update,name="update"),
    path('add/',views.add,name="add"),
    path('delete/<int:id>/',views.delete,name="delete"),
]