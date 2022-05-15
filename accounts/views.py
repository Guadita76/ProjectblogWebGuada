from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from .models import Profile
from django.contrib import messages
from accounts.forms import  UserRegisterForm, ProfilePageForm
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
#from django.views.generic import DetailView
from django.views.generic import DetailView,UpdateView, CreateView



class UserRegisterView(generic.CreateView):
    form_class= UserRegisterForm
    template_name= 'accounts/register.html'
    success_url= reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class= UserChangeForm
    template_name= 'accounts/edit_user.html'
    success_url= reverse_lazy('home')
    
    def get_object(self):
        return self.request.user



class PasswordsChangeView(PasswordChangeView):
    
    form_class= PasswordChangeForm
    success_url= reverse_lazy('home')
    
 
 
class ShowProfilePageView(DetailView):
        model= Profile
        template_name= 'accounts/show_profile.html'
        
        def get_context_data(self, *args, **kwargs):
            #users= Profile.objects.all()
            context= super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
                
            page_user= get_object_or_404(Profile, id=self.kwargs['pk']) 
            context['page_user']= page_user
            return context
        
        
class EditProfilePageView(generic.UpdateView):
    model= Profile
    template_name= 'accounts/edit_profile_page.html'
    fields= ['link', 'bio', 'image']
    success_url= reverse_lazy('home')
    
    
class CreateProfilePageView(CreateView):
    model= Profile
    #fields= '__all__'
    form_class= ProfilePageForm
    template_name= 'accounts/create_profile_page.html'
    success_url= reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.user= self.request.user
        return super().form_valid(form)
    
    
    
    
    
    
    



def Profiles (request, username= None):
    
    current_user = request.user
    if username and username != current_user.username:
        user= User.objects.get (username= username)
        posts= user.posts.all()
       
    else:
        posts= current_user.posts.all()  
        user= current_user
       
    return render (request, 'accounts/profile.html', {'user': user, 'posts': posts })







    

    
    
    



