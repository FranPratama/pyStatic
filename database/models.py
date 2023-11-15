from django.db import models

# Create your models here.
class Gender(models.Model):
    codeG = models.CharField(max_length=5)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    codePro = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    vers = models.CharField(max_length=50)
    stock = models.IntegerField()
    price = models.BigIntegerField()
    link_pic = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return "{}. {}".format(self.codePro,self.name)

class Order(models.Model):
    name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender ,on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    order = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.name,self.name)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender ,on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    testimonials = models.TextField(max_length=500)

    def __str__(self):
        return "{}. {}".format(self.name,self.testimonials)