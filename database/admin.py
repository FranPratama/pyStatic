from django.contrib import admin

# Register your models here.
from .models import *

class columnProduct(admin.ModelAdmin):
    list_display = ['codePro', 'name', 'vers', 'stock', 'price', 'link_pic']
    search_fields = ['codePro', 'name']
    list_filter = ('price',)
    list_per_page = 10

class columnOrder(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address', 'phone_number', 'email', 'order']
    search_fields = ['name', 'order']
    list_filter = ('order',)
    list_per_page = 10

class columnTestimonial(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address', 'phone_number', 'email', 'testimonials']
    search_fields = ['name', 'testimonials']
    list_filter = ('testimonials',)
    list_per_page = 10

admin.site.register(Order, columnOrder)
admin.site.register(Gender)
admin.site.register(Testimonial, columnTestimonial)
admin.site.register(Product, columnProduct)