
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Avatar(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen=models.ImageField (upload_to= 'avatar', null= True, blank= True, default= '2.jpg')
    
    
    
    
class Profile (models.Model):
    
    user= models.OneToOneField(User, null= True ,unique= True, on_delete=models.CASCADE)
    link= models.URLField(null=True)
    bio= models.TextField(default= 'Acerca de mi...', max_length=100)
    image=models.ImageField ( upload_to= "avatares", null= True, blank= True)
    
    
    def __str__(self):
        return f' Perfil de: {self.user.username}'
    
    
