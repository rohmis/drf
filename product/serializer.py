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

class CategorySerializer(serializers.ModelSerializer):
    
    category_name=serializers.CharField()
    category=BlogSerializer(many=True, read_only=True)
    
    class Meta:
        model=Category
        exclude=['id']