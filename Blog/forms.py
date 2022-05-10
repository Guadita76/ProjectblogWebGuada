from django import forms
from django.contrib.auth.models import User
from Blog.models import *
from ckeditor.fields import RichTextField
from django.utils import timezone

    



class PostForm (forms.ModelForm):
    
    
    title= forms.CharField(label= 'Titulo' ,max_length=40)
    sub_title=forms.CharField(label= 'Sub Titulo',max_length=40)   
    content= RichTextField()
    #timestamp=forms.DateTimeField()
    #image= forms.ImageField (required=False)
                     
                        
    class Meta:
        model=Post
        fields= ['title', 'sub_title','content', 'timestamp', 'image']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ['name','content']
        
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
