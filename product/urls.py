from django.urls import path, include
from . import views


urlpatterns = [
    path('blog_list/', views.BlogListCreateView.as_view(),name="blog_list"),
    path("blog_detail/<int:pk>/",views.BlogDetailView.as_view(),name="blog_detail"),
    
    path('category_list/',views.CategoryListCreateView.as_view(),name="category_list"),
    path('category_detail/<int:pk>/',views.CategoryDetailView.as_view(),name="category_detail"),
    
    path('blog_comment_list/<int:blog_id>/',views.BlogCommentListCreateView.as_view(),name="blog_comment_list"),
    
    

]

