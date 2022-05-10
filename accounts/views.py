from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.contrib import messages
from accounts.forms import EditProfileForm, UserRegisterForm, ProfilePageForm
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView



def register (request):

    if request.method == 'POST':
        
        form= UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            username= form.cleaned_data['username']
           
            messages.success(request, f'Usuario {username} creado')
            return redirect ('home')
    else:    
            
        form= UserRegisterForm()
            
       
            
    return render (request, 'accounts/register.html',{'form': form})    



def Profiles (request, username= None):
    
    current_user = request.user
    if username and username != current_user.username:
        user= User.objects.get (username= username)
        posts= user.posts.all()
       
    else:
        posts= current_user.posts.all()  
        user= current_user
       
    return render (request, 'accounts/profile.html', {'user': user, 'posts': posts })






class EditProfilePageView(generic.UpdateView):
    model= Profile
    template_name= 'accounts/edit_profile_page.html'
    fields= ['link', 'bio', 'image']
    success_url= reverse_lazy('home')
    

    
    
    
class PasswordsChangeView(PasswordChangeView):
    
    form_class= PasswordChangeForm
    success_url= reverse_lazy('home')
    
 
class UserEditView(generic.UpdateView):
    form_class= UserChangeForm
    template_name= 'accounts/edit_profile.html'
    success_url= reverse_lazy('home')
    
    def get_object(self):
        return self.request.user


class CreateProfilePageView(CreateView):
    model= Profile
    form_class= ProfilePageForm
    template_name= 'accounts/user_profile.html'
    
    
    def form_valid(self,form):
        form.instance.user= self.request.user
        return super().form_valid(form)
    
    
    