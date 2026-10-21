from decimal import Decimal

from django.core.management.base import BaseCommand

from store.management.commands.seed_data import SCREENSHOT_PRODUCTS
from store.models import Product


class Command(BaseCommand):
    help = "Refresh 12 products with exact updated user prices and descriptions."

    def handle(self, *args, **kwargs):
        screenshot_map = {item["name"]: item for item in SCREENSHOT_PRODUCTS}
        updated = 0

        for product in Product.objects.all():
            if product.name in screenshot_map:
                item = screenshot_map[product.name]
                product.code = item["code"]
                product.price = item["price"]
                product.old_price = item["old_price"]
                product.description = item["description"]
                product.image = ""
                product.image_url = f"/static/store/images/products/{item['image_file']}"
                product.featured = True
                product.save()
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated {updated} products with exact prices and descriptions."
            )
        )
