from django.contrib import admin
from .models import (
    Campaign,
    CampaignRecipient,
    Cart,
    CartItem,
    Category,
    Inventory,
    MaintenanceReminder,
    Order,
    OrderItem,
    Product,
    Profile,
    Review,
    ServiceRequest,
    Wishlist,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'price', 'old_price', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name', 'code', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register([
    Profile,
    Category,
    Inventory,
    Cart,
    CartItem,
    Wishlist,
    Order,
    OrderItem,
    Review,
    ServiceRequest,
    MaintenanceReminder,
    Campaign,
    CampaignRecipient,
])
