from django import forms
from .models import *



class Login(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
            ]
        widgets = {
            'name': forms.TextInput(attrs = { 'class' : 'form-control' }),
        }



class Loginform(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'auther',
            'book_photo',
            'auther_photo',
            'pages',
            'price',
            'price_day_rent',
            'period_rent',
            'status',
            'category',
            'total_rental',
            ]

        widgets = {
            'title': forms.TextInput(attrs = { 'class' : 'form-control' }),
            'auther': forms.TextInput(attrs = { 'class' : 'form-control' }),
            'book_photo': forms.FileInput(attrs = { 'class' : 'form-control' }),
            'auther_photo': forms.FileInput(attrs = { 'class' : 'form-control' }),
            'pages': forms.NumberInput(attrs = { 'class' : 'form-control' }),
            'price': forms.NumberInput(attrs = { 'class' : 'form-control' }),
            'price_day_rent': forms.NumberInput(attrs = { 'class' : 'form-control', 'id':'rentalprice' }),
            'period_rent': forms.NumberInput(attrs = { 'class' : 'form-control', 'id':'rentalperiod' }),
            'total_rental': forms.NumberInput(attrs = { 'class' : 'form-control', 'id':'profittotal' }),
            'status': forms.Select(attrs = { 'class' : 'form-control' }),
            'category': forms.Select(attrs = { 'class' : 'form-control' }),
        }


