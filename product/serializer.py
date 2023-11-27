from rest_framework import serializers
from product.models import Blog,Category


        
class BlogSerializer(serializers.ModelSerializer):
    
    # id=serializers.IntegerField(read_only=True)
    # blog_title=serializers.CharField( validators =[blog_title_valid])
    # blog_description=serializers.CharField()
    # post_date=serializers.DateTimeField(required=False)
    # is_public=serializers.BooleanField()
    # slug=serializers.CharField(required=False)
    
    # len_blog_title=serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = "__all__"

# class CategorySerializer(serializers.ModelSerializer):
    
#     category_name=serializers.CharField()
#     category=BlogSerializer(many=True, read_only=True)
    
#     #  -------related fields-------------------
    
#     # category=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # category=serializers.StringRelatedField(many=True)
#     # category=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='blog_detail')
#     # category=serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    
#     class Meta:
#         model=Category
#         exclude=['id']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    category_name=serializers.CharField()
    category=BlogSerializer(many=True, read_only=True)
    
    #  -------related fields-------------------
    
    # category=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category=serializers.StringRelatedField(many=True)
    # category=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='blog_detail')
    # category=serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    
    class Meta:
        model=Category
        fields='__all__'