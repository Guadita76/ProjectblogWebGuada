
from django.urls import include, path
from Blog import views



urlpatterns = [
    
    path ('about/', views.about_me, name= 'about'),
    path('pages/', views.pages, name= 'pages'),
    path('post/', views.createPost, name = 'post'),
    path('editPost/<int:post_id>/', views.editPost, name= 'editPost'),
    path('delete/<int:post_id>/', views.deletePost, name= 'delete'),
    path('postdetail/<int:pk>/',views.PostDetailView.as_view(),name= 'postdetail'),
    path ('blog/pages/<int:pk>/comment/',views.AddCommentView.as_view(),name= 'add_comment'),
    
    
    
    
]