from .models import Blog,Category
from .serializer import BlogSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
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
            