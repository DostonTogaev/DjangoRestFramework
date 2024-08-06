from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Category

class CategorySerializer(ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Category
        fields = '__all__'


