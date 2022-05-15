
from django.urls import include, path
from Blog import views



urlpatterns = [
    
    path ('about/', views.about_me, name= 'about'),
    #path('pages/',views.PostView.as_view(), name = 'pages'),
    path('pages/', views.post_views, name= 'pages'),
    path('post/', views.createPost, name = 'post'),
    #path('edit_post<int:pk>/', views.EditPostView.as_view(), name= 'edit_post'),
    path('editPost/<int:post_id>/', views.editPost, name= 'editPost'),
    path('delete/<int:post_id>/', views.deletePost, name= 'delete'),
    path('postdetail/<int:pk>/',views.PostDetailView.as_view(),name= 'postdetail'),
    path ('blog/pages/<int:pk>/comment/',views.AddCommentView.as_view(),name= 'add_comment'),
    
    
    
    
]