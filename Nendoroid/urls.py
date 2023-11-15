"""
URL configuration for Nendoroid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.shortcuts import render
from database.views import *

def home(request):
    title = "Home"
    context = {
        'title' : title,
    }

    return render(request, 'home.html', context)

def product(request):
    title = "Product"
    context = {
        'title' : title,
    }

    return render(request, 'product.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('product/',product),
    path('order/',order),
    path('testi/',testimony),
    path('vOrder/',vOrder),
    path('vTesti/',vTesti,name='vTesti'),
    path('update/<int:id_testi>',upTesti,name='upTesti'),
    path('delete/<int:id_testi>',delTesti,name='delTesti')
]