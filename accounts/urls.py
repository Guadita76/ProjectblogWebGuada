from django.urls import include, path
from .views import UserEditView, PasswordsChangeView,EditProfilePageView, CreateProfilePageView
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('login/', LoginView.as_view (template_name= 'accounts/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view (template_name= 'accounts/logout.html'), name= 'logout'),
    path('signup/', views.register , name= 'signup'),
    path('password/', PasswordsChangeView.as_view(template_name= 'accounts/change_password.html')),
    path('profile/<str:username>/',views.Profiles, name= 'profile'),
    #path('profile/',views.Profiles, name= 'profile'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile'),
    path('edit_profile_page/<int:pk>/',EditProfilePageView.as_view(), name= 'edit_profile_page'),
    path('create_profile/<int:pk>/', CreateProfilePageView.as_view(), name= 'create_profile'),
   
   
     
   
  
] 