from .models import Blog,Category
from .serializer import BlogSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class CategoryListView(APIView):
    def get(self,request):
        all_Category= Category.objects.all()
        serializers=CategorySerializer(all_Category, many=True, context={'request':request})
        return Response(serializers.data)


class CategoryDetailView(APIView):
    def get(self,request,pk):
        single_Category= Category.objects.get(pk=pk)
        serializers=CategorySerializer(single_Category, context={'request':request})
        return Response(serializers.data)


# -------------Class base view---------------

# get and post

class BlogListView(APIView):
    def get(self, request):
        all_blogs= Blog.objects.filter(is_public=True)
        serializer= BlogSerializer(all_blogs ,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# get,put,delete

class BlogDetailView(APIView):
    
    def get(self, request, pk):
        blogs= Blog.objects.get(pk=pk)
        serializer= BlogSerializer(blogs)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
         blogs= Blog.objects.get(pk=pk)
         serializer= BlogSerializer(blogs,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request,pk):
          blog=Blog.objects.get(pk=pk)
          blog.delete()
          return Response(status=status.HTTP_200_OK)
        
        

# ---------------- json response ------------------------------

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



# --------function based api view---------------------------------



# @api_view(['GET','POST'])
# def blog_list(request):
#     if request.method == "GET":
#        all_blogs= Blog.objects.filter(is_public=True)
#        serializer= BlogSerializer(all_blogs ,many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
   
#     if request.method == "POST":
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
# @api_view(['GET','PUT','DELETE'])
# def blog_detail(request, pk):
#    if request.method == 'GET':
#      blogs= Blog.objects.get(pk=pk)
#      serializer= BlogSerializer(blogs)
#      return Response(serializer.data, status=status.HTTP_200_OK)
   
#    if request.method =='PUT':
#          blogs= Blog.objects.get(pk=pk)
#          serializer= BlogSerializer(blogs,data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status=status.HTTP_200_OK)
#          else:
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
#    if request.method  == 'DELETE':
#         blog=Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)