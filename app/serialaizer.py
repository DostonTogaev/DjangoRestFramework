from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Category, Group, Product, Comment, Image
from django.db.models import Avg

class CategorySerializer(ModelSerializer):
    image = serializers.ImageField(required=False)
    group_count = serializers.SerializerMethodField()
    def get_group_count(self, obj):
        return obj.groups.count()

    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    #category = CategorySerializer(read_only = True)
    category_slug = serializers.SlugField(source = 'category.slug')
    category_title = serializers.CharField(source = 'category.title')
    class Meta:
        model = Group
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    group_name = serializers.CharField(source = 'group.name')
    image_primary = serializers.SerializerMethodField()

    def get_image_primary(self, obj):
        # Tashqi modeldan birinchi rasmni olish
        first_image = obj.images.order_by('id').first()
        return first_image.image_url if first_image else None
    
    comment_rating = serializers.SerializerMethodField()
    def get_comment_rating(self, obj):
        return obj.Avg(comments.rating)
    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'