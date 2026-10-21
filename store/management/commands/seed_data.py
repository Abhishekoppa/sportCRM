from decimal import Decimal
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from store.fitness_celebrities import FITNESS_CELEBRITIES
from store.models import Category, Inventory, Product, Profile


SCREENSHOT_PRODUCTS = [
    {
        "name": "Hydration Pack",
        "code": "HP-001",
        "category": "Outdoor Gear",
        "price": Decimal("1500.00"),
        "old_price": Decimal("1999.00"),
        "image_file": "hydration_pack.jpg",
        "description": (
            "Stay hydrated on every adventure with this lightweight, high-capacity hydration pack. "
            "Designed for hikers, runners, and cyclists, it features an ergonomic, breathable harness, "
            "leak-proof water reservoir, and quick-access storage pockets for essentials like keys, trail snacks, and phone."
        ),
        "celebrity_name": "Vidyut Jammwal",
    },
    {
        "name": "Golf Clubs",
        "code": "GC-001",
        "category": "Equipment",
        "price": Decimal("30000.00"),
        "old_price": Decimal("36000.00"),
        "image_file": "golf_clubs.jpg",
        "description": (
            "Elevate your game with this precision-engineered golf club set. Designed for maximum distance, "
            "accuracy, and forgiveness on the course, each club features lightweight graphite shafts and "
            "durable stainless-steel heads to help golfers of all skill levels improve their swing and control."
        ),
        "celebrity_name": "Virat Kohli",
    },
    {
        "name": "Bicycle",
        "code": "BC-001",
        "category": "Equipment",
        "price": Decimal("15000.00"),
        "old_price": Decimal("18500.00"),
        "image_file": "bicycle.jpg",
        "description": (
            "Engineered for smooth commuting and weekend trail rides, this versatile bicycle combines a lightweight "
            "aluminum frame with smooth gear shifting and reliable dual-disc brakes. Enjoy ultimate comfort, stability, "
            "and control whether navigating city streets or tackling rugged paths."
        ),
        "celebrity_name": "Cristiano Ronaldo",
    },
    {
        "name": "Yoga Mat",
        "code": "YM-001",
        "category": "Equipment",
        "price": Decimal("1000.00"),
        "old_price": Decimal("1499.00"),
        "image_file": "yoga_mat.jpg",
        "description": (
            "Crafted for comfort, stability, and grip, this premium non-slip yoga mat provides optimal cushioning "
            "for joints during your daily yoga, Pilates, or floor workout routine. Lightweight, durable, and easy to roll up, "
            "it's perfect for practice at home or in the studio."
        ),
        "celebrity_name": "Hrithik Roshan",
    },
    {
        "name": "Snowboard",
        "code": "SN-001",
        "category": "Outdoor Gear",
        "price": Decimal("25000.00"),
        "old_price": Decimal("29500.00"),
        "image_file": "snowboard.jpg",
        "description": (
            "Built for mountain enthusiasts, this high-performance snowboard delivers excellent edge hold, speed, "
            "and maneuverability across all snow conditions. Featuring a responsive wood core and durable top sheet, "
            "it provides smooth turns and maximum stability from groomed runs to deep powder."
        ),
        "celebrity_name": "Arnold Schwarzenegger",
    },
    {
        "name": "Tennis Racquet",
        "code": "TR-001",
        "category": "Equipment",
        "price": Decimal("5000.00"),
        "old_price": Decimal("6499.00"),
        "image_file": "tennis_racquet.jpg",
        "description": (
            "Dominate the court with this lightweight, aerodynamically designed tennis racquet. Offering an ideal blend of "
            "power, control, and vibration damping, it helps players deliver precise groundstrokes, powerful serves, "
            "and quick responses at the net."
        ),
        "celebrity_name": "Rafael Nadal",
    },
    {
        "name": "Basketball Shoes",
        "code": "BS-001",
        "category": "Footwear",
        "price": Decimal("4000.00"),
        "old_price": Decimal("5299.00"),
        "image_file": "basketball_shoes.jpg",
        "description": (
            "Designed for explosive speed and multidirectional traction, these basketball shoes deliver superior ankle support "
            "and impact-absorbing midsole cushioning. The breathable mesh upper and grippy rubber outsole ensure top "
            "performance on indoor courts and outdoor pavements alike."
        ),
        "celebrity_name": "LeBron James",
    },
    {
        "name": "Treadmill",
        "code": "TM-001",
        "category": "Equipment",
        "price": Decimal("35000.00"),
        "old_price": Decimal("42000.00"),
        "image_file": "treadmill.jpg",
        "description": (
            "Bring the gym home with this advanced cardio treadmill. Equipped with a powerful motor, adjustable incline settings, "
            "shock-absorbing belt, and an intuitive digital display, it provides a smooth, customizable running or walking "
            "workout for every fitness level."
        ),
        "celebrity_name": "Dwayne Johnson",
    },
    {
        "name": "Skis",
        "code": "SK-001",
        "category": "Outdoor Gear",
        "price": Decimal("20000.00"),
        "old_price": Decimal("24500.00"),
        "image_file": "skis.jpg",
        "description": (
            "Conquer the slopes with confidence using these all-mountain skis. Engineered with a lightweight core and reinforced edges "
            "for high-speed stability and quick turn initiation, they offer unmatched performance on groomed trails and powder terrain alike."
        ),
        "celebrity_name": "Neeraj Chopra",
    },
    {
        "name": "Fitness Tracker",
        "code": "FT-001",
        "category": "Accessories",
        "price": Decimal("3500.00"),
        "old_price": Decimal("4699.00"),
        "image_file": "fitness_tracker.jpg",
        "description": (
            "Track your daily health and activity metrics with this sleek, feature-packed smart tracker. Monitors steps, distance, "
            "heart rate, sleep patterns, and active calories burned, featuring a crisp OLED screen and long-lasting battery life "
            "to keep you motivated all day long."
        ),
        "celebrity_name": "Cristiano Ronaldo",
    },
    {
        "name": "Moisture-Wicking Socks",
        "code": "MS-001",
        "category": "Apparel",
        "price": Decimal("500.00"),
        "old_price": Decimal("750.00"),
        "image_file": "wicking socks.jpeg",
        "description": (
            "Keep your feet cool, dry, and blister-free with these high-performance athletic socks. Crafted from advanced "
            "moisture-wicking fibers with reinforced arch support and extra heel cushioning, they provide long-lasting comfort "
            "during intense workouts or long days on your feet."
        ),
        "celebrity_name": "Virat Kohli",
    },
    {
        "name": "Running Shoes",
        "code": "RS-001",
        "category": "Footwear",
        "price": Decimal("3000.00"),
        "old_price": Decimal("3999.00"),
        "image_file": "running_shoes.jpg",
        "description": (
            "Engineered for runners seeking ultimate comfort and performance, these lightweight running shoes feature "
            "responsive foam cushioning and a breathable mesh upper. Designed to absorb impact and support smooth heel-to-toe "
            "transitions on road or treadmill runs."
        ),
        "celebrity_name": "Virat Kohli",
    },
]


class Command(BaseCommand):
    help = "Seed products with updated exact prices, word-for-word descriptions, and male athlete icons."

    def handle(self, *args, **kwargs):
        # 1. Categories (Product Families matching screenshot and requirements)
        cats_data = [
            ("Outdoor Gear", "/static/store/images/categories/outdoor_gear.jpg"),
            ("Equipment", "/static/store/images/categories/equipment.jpg"),
            ("Footwear", "/static/store/images/categories/footwear.jpg"),
            ("Accessories", "/static/store/images/categories/accessories.jpg"),
            ("Apparel", "/static/store/images/categories/apparel.jpg"),
        ]

        categories_map = {}
        for name, img in cats_data:
            cat, _ = Category.objects.get_or_create(
                name=name, defaults={"slug": slugify(name), "image": img}
            )
            cat.image = img
            cat.save(update_fields=["image"])
            categories_map[name] = cat

        # 2. Seed / Update the 12 Products with exact user prices & descriptions
        updated_count = 0

        for item in SCREENSHOT_PRODUCTS:
            cat = categories_map.get(item["category"], categories_map["Equipment"])
            slug = slugify(item["name"])
            local_static_url = f"/static/store/images/products/{item['image_file']}"
            p, _ = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    "category": cat,
                    "name": item["name"],
                    "code": item["code"],
                    "description": item["description"],
                    "price": item["price"],
                    "old_price": item["old_price"],
                    "image": "",
                    "image_url": local_static_url,
                    "featured": True,
                },
            )

            p.category = cat
            p.name = item["name"]
            p.code = item["code"]
            p.description = item["description"]
            p.price = item["price"]
            p.old_price = item["old_price"]
            # Seeded product images are versioned static assets, not uploads.
            # This keeps catalog photos available on read-only/serverless hosts.
            p.image = ""
            p.image_url = local_static_url
            p.featured = True
            p.save()

            Inventory.objects.get_or_create(
                product=p, defaults={"quantity": 30, "reorder_level": 5}
            )
            updated_count += 1

        # Keep the catalog limited to the 12 products in the approved list.
        allowed_slugs = [slugify(item["name"]) for item in SCREENSHOT_PRODUCTS]
        Product.objects.exclude(slug__in=allowed_slugs).delete()

        # 3. Ensure sample users exist
        for i in range(1, 4):
            u, _ = User.objects.get_or_create(
                username=f"customer{i}",
                defaults={"email": f"customer{i}@example.com"},
            )
            u.set_password("Sportiva123!")
            u.save()
            Profile.objects.get_or_create(user=u)

        admin, _ = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@sportiva.local",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin.set_password("Admin123!")
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        Profile.objects.get_or_create(user=admin)

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated all 12 products with exact prices & descriptions. (Count: {updated_count})"
            )
        )
