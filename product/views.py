from .models import Blog,Category,BlogComment
from .serializer import BlogSerializer,CategorySerializer,BlogCommentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsAdminUserOrReadOnly


# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    
    # custom permissions
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer=CategorySerializer(queryset, many=True, context={'request':request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No Category Found'},status=status.HTTP_204_NO_CONTENT)
        
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def retrieve(self, request, *args, **kwargs):
            instance=self.get_object()
            serializer= self.get_serializer(instance)
            
            if instance:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'Message':'No Blog Found'}, status=status.HTTP_404_NOT_FOUND)
            



class BlogListCreateView(generics.ListCreateAPIView):
    queryset=Blog.objects.filter(is_public=True)
    serializer_class=BlogSerializer
    
    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        serializer= BlogSerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blogs Found'},status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer= BlogSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)
    
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
       queryset=Blog.objects.filter(is_public=True)
       serializer_class=BlogSerializer
    #    lookup_field='id'
       
       def retrieve(self, request, *args, **kwargs):
            instance=self.get_object()
            serializer= self.get_serializer(instance)
            
            if instance:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'Message':'No Blog Found'}, status=status.HTTP_404_NOT_FOUND)
            
            
class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset=BlogComment.objects.all()
    serializer_class=BlogCommentSerializers
    
    def get_queryset(self):
        blog_id= self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
       blog_id= self.kwargs.get('blog_id')
       blog=get_object_or_404(Blog,id=blog_id)
       if BlogComment.objects.filter(blog=blog,author=self.request.user).exists():
           raise serializer.ValidationError({'message':'you have already added comment on this blog'})
       serializer.save(author=self.request.user,blog=blog)