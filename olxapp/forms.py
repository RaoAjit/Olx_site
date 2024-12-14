from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Product


class Register(UserCreationForm):
    gender=forms.CharField(max_length=20,required=True)
    email=forms.EmailField(max_length=50,required=True)
 
    class Meta:
        model=User
        fields=('username','gender','email','password1','password2')


        
    



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price','address','contact_no','image','type']


