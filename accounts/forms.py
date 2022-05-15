from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from email.policy import default

from .models import *



class UserRegisterForm (UserCreationForm):
    
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repita la Contraseña', widget= forms.PasswordInput)
    

    class Meta:
    
       model= User
       fields= ['username','first_name', 'last_name' ,'email','password1', 'password2']
       help_texts= {k: "" for k in fields}
       
       
       

# class EditProfileForm (forms.Form):
#     first_name= forms.CharField (label= "Nombre", max_length= 20)
#     last_name= forms.CharField (label= "Apellido", max_length= 20)
#     email= forms.EmailField()
#     link= forms.URLField(required= False)
#     bio= forms.CharField(widget= forms.Textarea,max_length=100)
#     image=forms.ImageField ( )
#     password1= forms.CharField(label= "Contraseña",widget= forms.PasswordInput, required= False) 
#     password2= forms.CharField(label= "Repetir  Contraseña",widget= forms.PasswordInput, required= False)
    
#     class Meta:
#         model=Profile
#         fields= ['user','link', 'bio','image']
#         help_texts= {k: "" for k in fields}
    
#     class Meta:
#         model= User
#         fields= ['first_name', 'last_name','email', 'password1', 'password2']
#         help_texts= {k: "" for k in fields}
    
    

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ('bio','link','image')
        
    widgets= {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.Textarea(attrs={'class': 'form-control'}),
            #'image': forms.Textarea(attrs={'class': 'form-control'}),
        }