from django.urls import path
from . import views

urlpatterns = [
    # path('blog_list/',views.blog_list,name="blog_list"),
    # path('blog_detail/<int:pk>/',views.blog_detail,name="blog_detail"),
    
    # class based view url
    # path('blog_list/',views.BlogListView.as_view(),name="blog_list"),
    # path('blog_detail/<int:pk>/',views.BlogDetailView.as_view(),name="blog_detail"),
    # path('category_list/',views.CategoryListView.as_view(),name="category_list"),
    # path('category_detail/<int:pk>/',views.CategoryDetailView.as_view(),name="category-detail"),
    
    # # --Generic views links--
    # path('blog_list_generic_view/',views.BlogListGenericView.as_view(),name="blog_list_generic_view"),
    #  path('blog_detail_generic_view/<str:slug>/',views.BlogDetailGenericView.as_view(),name="blog_detail_generic_view"),
    
    path('blog_list_creatapiview/',views.BlogListCon.as_view(),name="blog_list_createapiview"),
    path('blog_list/',views.BlogList.as_view(),name="blog_list"),
    path('blog_list_retrieve/<int:pk>/',views.BlogListRetrieve.as_view(),name="blog_list_retrieve"),
    path('blog_destroy/<int:pk>/',views.BlogDestroyCon.as_view(),name="blog_destroy"),
    path('blog_update/<int:pk>/',views.BlogUpdateCon.as_view(),name="blog_update"),
]

