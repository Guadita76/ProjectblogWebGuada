from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse





class Post (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title= models.CharField(max_length=250, null= False)
    sub_title=models.CharField(max_length=100, null= True)
    content= RichTextField()
    timestamp=models.DateTimeField(default=timezone.now)
    image=models.ImageField (upload_to= "posts", null= True, default='placeholder.png' )
    
    
    class Meta:
        ordering = ['-timestamp']
        
        
    def __str__(self):
          return f' {self.user.username} : {self.title}'
      
    def get_absolute_url(self):
        return reverse("home")
    
    
   


class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=100, null= False)
    content= models.TextField()
    timestamp=models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-timestamp']
        
        
    def __str__(self):
          return '%s - %s' % (self.post.title, self.name)
      
      
 
    
    