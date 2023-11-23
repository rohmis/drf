from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# def blog_list(request):
    
#     blogs=Blog.objects.all()
    
#     data={
#         "Blogs": list(blogs.values())
#     }
#     return JsonResponse(data)

# def blog_detail(request,pk):
    
#     blogs=Blog.objects.get(pk=pk)
    
#     data={
#        'name':blogs.name,
#        'description':blogs.description,
#        'slug':blogs.slug,
#     }
#     return JsonResponse(data)

@api_view(['GET'])
def blog_list(request):
     all_blogs= Blog.objects.filter(is_public=True)
     serializer= BlogSerializer(all_blogs ,many=True)
     return Response(serializer.data)
 
@api_view(['GET'])
def blog_detail(request, pk):
     blogs= Blog.objects.get(is_public=True, pk=pk)
     serializer= BlogSerializer(blogs)
     return Response(serializer.data)