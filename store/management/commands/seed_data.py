from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import *
from django.utils.text import slugify
from django.utils import timezone
from datetime import timedelta
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  cats=[('Footwear','https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80'),('Sportswear','https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=900&q=80'),('Fitness Equipment','https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=900&q=80'),('Outdoor Gear','https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=900&q=80'),('Accessories','https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80')]
  categories=[]
  for n,img in cats: categories.append(Category.objects.get_or_create(name=n,defaults={'slug':slugify(n),'image':img})[0])
  names=['Velocity Runner','Aero Trainer','Court Pro','Trail Blazer','Sprint Elite','Core Tee','Motion Shorts','Pro Jacket','Flex Leggings','Endurance Hoodie','Power Dumbbells','Kettlebell 16kg','Resistance Bands','Yoga Mat Pro','Adjustable Bench','Trek Backpack','Hydration Pack','Trail Tent','Climb Harness','Outdoor Jacket','Smart Sports Watch','Performance Socks','Training Gloves','Shaker Bottle','Gym Towel','Foam Roller','Skipping Rope','Sports Cap','Knee Support','Performance Bottle']
  imgs=['https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80','https://images.unsplash.com/photo-1546483875-ad9014c88eba?auto=format&fit=crop&w=900&q=80','https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=900&q=80','https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=900&q=80']
  for i,n in enumerate(names):
   c=categories[i%5]; p,_=Product.objects.get_or_create(slug=slugify(n),defaults={'category':c,'name':n,'description':f'Premium SPORTIVA {n.lower()} built for training, competition and everyday performance.','price':1499+(i*173)%8500,'old_price':1999+(i*211)%10000,'image_url':imgs[i%4],'featured':i<12}); Inventory.objects.get_or_create(product=p,defaults={'quantity':10+i,'reorder_level':5})
  for i in range(1,4):
   u,_=User.objects.get_or_create(username=f'customer{i}',defaults={'email':f'customer{i}@example.com'}); u.set_password('Sportiva123!'); u.save(); Profile.objects.get_or_create(user=u)
  admin,_=User.objects.get_or_create(username='admin',defaults={'email':'admin@sportiva.local','is_staff':True,'is_superuser':True}); admin.set_password('Admin123!'); admin.is_staff=True; admin.is_superuser=True; admin.save(); Profile.objects.get_or_create(user=admin)
  self.stdout.write(self.style.SUCCESS('SPORTIVA seed complete: 30 products, sample customers and admin.'))
