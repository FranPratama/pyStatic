from django.forms import ModelForm
from database.models import *
from django import forms

class FormOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
            'gender' : forms.Select({'class':'form-control'}),
            'address' : forms.Textarea({'class':'form-control'}),
            'phone_number' : forms.NumberInput({'class':'form-control'}),
            'email' : forms.EmailInput({'class':'form-control'}),
            'order' : forms.Select({'class':'form-control'})
        }

class FormTestimony(ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
            'gender' : forms.Select({'class':'form-control'}),
            'address' : forms.Textarea({'class':'form-control'}),
            'phone_number' : forms.NumberInput({'class':'form-control'}),
            'email' : forms.EmailInput({'class':'form-control'}),
            'testimonials' : forms.Textarea({'class':'form-control'})
        }