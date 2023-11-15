from django.shortcuts import render, redirect
from django.contrib import messages
from database.forms import *
from database.models import *

# Create your views here.
def order(request):
    if request.POST:
        form = FormOrder(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order successfully added !!")
            form = FormOrder()
            title = "Order"
            context = {
                'form':form,
                'title':title,
            }
            return render(request, 'order.html', context)
    else:
        form = FormOrder()
        title = "Order"
        context = {
            'form':form,
            'title':title,
        }
    return render(request,'order.html',context)

def vOrder(request):
    view = Order.objects.all()
    title = "View Cart"
    context = {
        'view':view,
        'title':title,
    }

    return render(request, 'vOrder.html', context)

def testimony(request):
    if request.POST:
        form = FormTestimony(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimony has been sent, thank you for your purchase~")
            form = FormTestimony()
            title = "Testimony"
            context = {
                'form':form,
                'title':title,
            }
            return render(request, 'testimony.html', context)
    else:
        form = FormTestimony()
        title = "Testimony"
        context = {
            'form':form,
            'title':title,
        }
    return render(request,'testimony.html',context)

def vTesti(request):
    view = Testimonial.objects.all()
    title = "View Testimony"
    context = {
        'view':view,
        'title':title,
    }

    return render(request, 'vTesti.html', context)

def upTesti(request,id_testi):
    testi = Testimonial.objects.get(id=id_testi)
    if request.POST:
        form = FormTestimony(request.POST,instance=testi)
        if form.is_valid():
            form.save()
            messages.success(request,"Testimony successfully updated~")
            return redirect('upTesti',id_testi=id_testi)
    else:
        form = FormTestimony(instance=testi)
        title = "Update Testimony"
        context = {
            'form':form,
            'testi':testi,
            'title':title
        }
    return render(request,'upTesti.html',context)

def delTesti(request,id_testi):
    testi = Testimonial.objects.filter(id=id_testi)
    testi.delete()
    messages.success(request,"Testimony successfully deleted !!")
    return redirect('vTesti')