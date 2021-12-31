from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class register(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.user)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Poster(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    profile_picture = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    Name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(null=True)
    content = models.TextField()


class Category(models.Model):
    cat=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.cat

    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    content  = models.CharField(max_length=100,default=True)
    badge = models.CharField(max_length=100,null=True)
    stock=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    


    
class cart_items(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cart_item'

    
    def __str__(self):
        return str(self.product)

  
    def sub_total(self):
        return self.quantity * self.product.price

    def total(self,total=0):
        total += (self.quantity * self.product.price)
        return total
    
   
class Wishlist(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)
    