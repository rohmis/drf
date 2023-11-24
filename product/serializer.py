from rest_framework import serializers
from product.models import Blog

def name_valid(value):
        if len(value)< 4:
            raise serializers.ValidationError("Blog title is very short")
        else:
            return value
        
class BlogSerializer(serializers.ModelSerializer):
    
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField( validators =[name_valid])
    description=serializers.CharField()
    post_date=serializers.DateField()
    is_public=serializers.BooleanField()
    slug=serializers.CharField()
    
    class Meta:
        model = Blog
        fields = "__all__"
    
    # Field-level-validation
    # def validate_name(self, value):
    #     if len(value)< 4:
    #         raise serializers.ValidationError("Blog title is very short")
    #     else:
    #         return value
        
    # object-level-validation
    def validate(self,data):
        if data['name']== data['description']:
            raise serializers.ValidationError("Blog title and description can not be same")
        else:
            return data
        
    # validators
    
        
        
            

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