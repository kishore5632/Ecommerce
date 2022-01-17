from rest_framework import serializers
from carts.models import *
from rest_framework.serializers import ModelSerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class Cart_item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = cart_items
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = "__all__"



