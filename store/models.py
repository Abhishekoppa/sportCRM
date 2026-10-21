from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):
 user=models.OneToOneField(User,on_delete=models.CASCADE); phone=models.CharField(max_length=20,blank=True); address=models.TextField(blank=True); loyalty_points=models.PositiveIntegerField(default=0)
 def __str__(self): return self.user.username

class Category(models.Model):
 name=models.CharField(max_length=80,unique=True)
 slug=models.SlugField(unique=True)
 image=models.URLField(blank=True)
 parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="subcategories")
 def __str__(self): return self.name

class Product(models.Model):
 category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products'); name=models.CharField(max_length=160); code=models.CharField(max_length=50,blank=True,default=''); slug=models.SlugField(unique=True); description=models.TextField(); price=models.DecimalField(max_digits=10,decimal_places=2); old_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True); image=models.ImageField(upload_to='products/',blank=True); image_url=models.CharField(max_length=500,blank=True,default=''); featured=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
 def get_image(self):
  if self.image: return self.image.url
  if self.image_url: return self.image_url
  return '/static/store/images/products/running_shoes.jpg'
 def get_absolute_url(self): return reverse('product',args=[self.slug])
 @property
 def celebrity(self):
  from .fitness_celebrities import get_celebrity_for_product
  return get_celebrity_for_product(self.name)
 @property
 def rating(self):
  vals=list(self.reviews.values_list('rating',flat=True)); return round(sum(vals)/len(vals),1) if vals else 0

class Inventory(models.Model):
 product=models.OneToOneField(Product,on_delete=models.CASCADE,related_name='inventory'); quantity=models.PositiveIntegerField(default=0); reorder_level=models.PositiveIntegerField(default=5)
 @property
 def status(self): return 'In Stock' if self.quantity>self.reorder_level else ('Low Stock' if self.quantity else 'Out of Stock')

class Cart(models.Model): user=models.OneToOneField(User,on_delete=models.CASCADE)

class CartItem(models.Model):
 cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items'); product=models.ForeignKey(Product,on_delete=models.CASCADE); quantity=models.PositiveIntegerField(default=1)
 @property
 def total(self): return self.product.price*self.quantity

class Wishlist(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='wishlist'); product=models.ForeignKey(Product,on_delete=models.CASCADE)
 class Meta: unique_together=('user','product')

class Order(models.Model):
 STATUS=[('PLACED','Placed'),('PROCESSING','Processing'),('SHIPPED','Shipped'),('DELIVERED','Delivered')]
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders'); created_at=models.DateTimeField(auto_now_add=True); status=models.CharField(max_length=20,choices=STATUS,default='PLACED'); total=models.DecimalField(max_digits=10,decimal_places=2); address=models.TextField()

class OrderItem(models.Model): order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items'); product=models.ForeignKey(Product,on_delete=models.PROTECT); quantity=models.PositiveIntegerField(); price=models.DecimalField(max_digits=10,decimal_places=2)

class Review(models.Model):
 product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews'); user=models.ForeignKey(User,on_delete=models.CASCADE); rating=models.PositiveIntegerField(); comment=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)

class ServiceRequest(models.Model):
 TYPES=[('SUPPORT','Support'),('RETURN','Return'),('REPAIR','Repair')]; user=models.ForeignKey(User,on_delete=models.CASCADE); request_type=models.CharField(max_length=20,choices=TYPES); subject=models.CharField(max_length=160); description=models.TextField(); status=models.CharField(max_length=30,default='Open'); created_at=models.DateTimeField(auto_now_add=True)

class MaintenanceReminder(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE); title=models.CharField(max_length=160); due_date=models.DateField(); notes=models.TextField(blank=True); completed=models.BooleanField(default=False)

class Campaign(models.Model):
 name=models.CharField(max_length=160); description=models.TextField(); discount_percent=models.PositiveIntegerField(default=10); starts=models.DateTimeField(default=timezone.now); ends=models.DateTimeField(); active=models.BooleanField(default=True)

class CampaignRecipient(models.Model):
 campaign=models.ForeignKey(Campaign,on_delete=models.CASCADE); customer=models.ForeignKey(User,on_delete=models.CASCADE); sent_at=models.DateTimeField(auto_now_add=True)