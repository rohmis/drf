from rest_framework import serializers
from product.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


# --------------simple Serializer-----------------

# class BlogSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     # author=serializers.CharField()
#     description=serializers.CharField()
#     post_date=serializers.DateField()
#     is_public=serializers.BooleanField()
#     slug=serializers.CharField()
    
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name= validated_data.get('name',instance.name)
#         instance.description= validated_data.get('description',instance.description)
#         instance.post_date= validated_data.get('post_date',instance.post_date)
#         instance.is_public= validated_data.get('is_public',instance.is_public)
#         instance.slug= validated_data.get('slug',instance.slug)
#         instance.save()
#         return instance 