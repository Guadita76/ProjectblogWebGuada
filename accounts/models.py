
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Avatar(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen=models.ImageField (upload_to= 'avatar', null= True, blank= True, default= '2.jpg')
    
    
    
    
class Profile (models.Model):
    
    user= models.OneToOneField(User, null= True ,on_delete=models.CASCADE)
    link= models.URLField(null=True)
    bio= models.TextField(default= 'Acerca de mi...', max_length=100)
    image=models.ImageField ( upload_to= "avatares", null= True, blank= True)
    
    
    def __str__(self):
        return f' Perfil de: {self.user.username}'
    
    
    def following (self):
        user_ids=Relationship.objects.filter(from_user= self.user)\
                                    .values_list('to_user_id', flat= True)
    
        return  User.objects.filter(id__in= user_ids)
    
    
    def followers(self):
        user_ids=Relationship.objects.filter(to_user= self.user)\
                                    .values_list('from_user_id', flat= True)
    
        return  User.objects.filter(id__in= user_ids)
    
    
    
class Relationship(models.Model):
    from_user= models.ForeignKey(User, related_name= 'relationship', on_delete=models.CASCADE )
    to_user= models.ForeignKey(User, related_name= 'related_to', on_delete=models.CASCADE )
        
        
    def __str__(self):
            return f'{self.from_user} to {self.to_user}'
        
    class Meta:
            indexes= [
                models.Index(fields=['from_user', 'to_user'])
            ]