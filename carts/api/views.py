from .serializers import *
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser




#api views

class Product_add_update_delete(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class product_list(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Category_list(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Category_add_update_delete(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class Comment_list(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Comment_delete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Poster_add_update_delete(viewsets.ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    permission_classes = [IsAdminUser]

class Poster_list(generics.ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class Cart_view(viewsets.ModelViewSet):
    queryset = cart_items.objects.all()
    serializer_class = Cart_item_Serializer





        
    

  
    

   
 














