from django.contrib import admin
from .models import *
admin.site.register([Profile,Category,Product,Inventory,Cart,CartItem,Wishlist,Order,OrderItem,Review,ServiceRequest,MaintenanceReminder,Campaign,CampaignRecipient])
