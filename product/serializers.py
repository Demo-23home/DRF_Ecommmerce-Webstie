from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"        



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"