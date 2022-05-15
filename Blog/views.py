from msilib.schema import ListView
from tkinter import PAGES
from django.shortcuts import get_object_or_404, render, redirect
from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from Blog.forms import PostForm, CommentForm
from Blog.models import Post, Comment
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView, ListView


# Create your views here.


def home (request):
    
    return render (request,'blog/index.html')


def about_me (request):
    
   return render (request, 'blog/about_me.html')


# class PostView(ListView):
#     model= Post
#     template_name= 'blog/pages.html'
#     paginate_by= 3
    
    
    
# class EditPostView(DetailView) :  
#     form_class= PostForm
#     template_name= 'blog/edit_post.html'
#     success_url= reverse_lazy('home')
    
    
    
def post_views (request):
    
    posts= Post.objects.all()
       
    paginator= Paginator(posts,3)
    page= request.GET.get('page')
    posts= paginator.get_page(page)   
    
    return render (request, 'blog/pages.html', {'posts': posts})





class PostDetailView(DetailView):
   
    template_name = 'blog/postdetail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'pk'

class AddCommentView(CreateView):
    model= Comment
    form_class= CommentForm
    template_name= 'blog/add_comment.html'
    #fields= '__all__'
    def form_valid(self, form):  
        form.instance.post_id = self.kwargs['pk']   
        return super().form_valid(form)
    success_url= reverse_lazy('home')
    
    

def createPost (request):
    
    current_user= get_object_or_404( User, pk= request.user.pk)
    if request.method == 'POST':
        
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.user = current_user
            post.save()
            title= form.cleaned_data.get('title')
            messages.success(request,f'El Post {title}, ha sido creado correctamente')
            return redirect ('pages')
    
    else:
        form= PostForm()
           
        
    return render (request, 'blog/post.html', {'form': form})  



def editPost (request, post_id=None):
    post= Post.objects.get(id=post_id)
    form= PostForm(instance=post)
    
    if request.method == 'POST':
        
        form= PostForm(request.POST, request.FILES, instance=post)
      
        if form.is_valid():
            info= form.cleaned_data
            post.title= info['title']
            post.sub_title= info['sub_title']
            post.content= info['content']
            post.image= info['image']
          
          
            post.save()  
            return redirect('pages')

    else:
        form= PostForm( initial={'title': post.title, 'sub_title': post.sub_title, 'content': post.content, 'image': post.image})
        
    return render (request, 'Blog/post.html', {'form': form, 'post_id': post_id})


def deletePost(request, post_id):
    post= Post.objects.get(id= post_id)
    post.delete()
    return redirect('pages')


   