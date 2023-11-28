from .models import Blog,Category
from .serializer import BlogSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

# Create your views here.

class BlogViewSet(viewsets.ViewSet):
    
    # def list(self, request):
    #     queryset = Blog.objects.filter(is_public=True)
    #     serializer = BlogSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Blog.objects.filter(is_public=True)
    #     blog_list = get_list_or_404(queryset, pk=pk)
    #     serializer = BlogSerializer(blog_list)
    #     return Response(serializer.data)
    
    def list(self, request):
        queryset = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Blog.objects.filter(is_public=True)
        blog_list = get_object_or_404(queryset, pk=pk)
        serializer = BlogSerializer(blog_list)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer= BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        blog=get_object_or_404(Blog, pk=pk)
        serializer= BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        blog = get_object_or_404(Blog,pk=pk)
        blog.delete()
        return Response({"Message": "your blog is deleted"}, status=status.HTTP_204_NO_CONTENT)


# class CategoryListView(APIView):
#     def get(self,request):
#         all_Category= Category.objects.all()
#         serializers=CategorySerializer(all_Category, many=True, context={'request':request})
#         return Response(serializers.data)


# class CategoryDetailView(APIView):
#     def get(self,request,pk):
#         single_Category= Category.objects.get(pk=pk)
#         serializers=CategorySerializer(single_Category, context={'request':request})
#         return Response(serializers.data)


# # -------------Class base view---------------

# # get and post

# class BlogListView(APIView):
#     def get(self, request):
#         all_blogs= Blog.objects.filter(is_public=True)
#         serializer= BlogSerializer(all_blogs ,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# # get,put,delete

# class BlogDetailView(APIView):
    
#     def get(self, request, pk):
#         blogs= Blog.objects.get(pk=pk)
#         serializer= BlogSerializer(blogs)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request,pk):
#          blogs= Blog.objects.get(pk=pk)
#          serializer= BlogSerializer(blogs,data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status=status.HTTP_200_OK)
#          else:
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
#     def delete(self, request,pk):
#           blog=Blog.objects.get(pk=pk)
#           blog.delete()
#           return Response(status=status.HTTP_200_OK)
        
        
# # -------------------------generic views-----------------------------------------

# class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Blog.objects.all()
#     serializer_class= BlogSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class BlogDetailGenericView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset=Blog.objects.all()
#     serializer_class= BlogSerializer
#     lookup_field='slug'
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#---------concrete api view---------------------------

# class BlogListCon(generics.CreateAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
# class BlogList(generics.ListAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
# class BlogListRetrieve(generics.RetrieveAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
#     # lookup_field='slug'
    
# # retriveDestroy api view
    
# class BlogRetrieveDestroyCon(generics.RetrieveDestroyAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
# class BlogListCreateCon(generics.ListCreateAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
# class BlogRetrieveUpdateCon(generics.RetrieveUpdateAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
    
