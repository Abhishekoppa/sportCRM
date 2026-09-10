from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category



class Command(BaseCommand):
    help = "Create SPORTIVA sports categories and subcategories"

    def handle(self, *args, **kwargs):

        categories = {
            "Cricket": {
                "image": "https://images.unsplash.com/photo-1531415074968-036ba1b575da",
                "subcategories": [
                    "Cricket Bats",
                    "Cricket Balls",
                    "Cricket Gloves",
                    "Cricket Helmets",
                    "Cricket Pads",
                    "Cricket Shoes",
                    "Cricket Bags",
                    "Cricket Protective Gear",
                    "Cricket Clothing",
                    "Cricket Accessories",
                ],
            },

            "Football": {
                "image": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55",
                "subcategories": [
                    "Footballs",
                    "Football Shoes",
                    "Jerseys",
                    "Shorts",
                    "Goalkeeper Gear",
                    "Shin Guards",
                    "Goal Nets",
                    "Football Bags",
                    "Accessories",
                ],
            },

            "Basketball": {
                "image": "https://images.unsplash.com/photo-1546519638-68e109498ffc",
                "subcategories": [
                    "Basketballs",
                    "Basketball Shoes",
                    "Jerseys",
                    "Shorts",
                    "Basketball Hoops",
                    "Nets",
                    "Training Equipment",
                    "Accessories",
                ],
            },

            "Badminton": {
                "image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea",
                "subcategories": [
                    "Badminton Rackets",
                    "Shuttlecocks",
                    "Badminton Shoes",
                    "Badminton Clothing",
                    "Racket Grips",
                    "Racket Strings",
                    "Badminton Bags",
                    "Accessories",
                ],
            },

            "Tennis": {
                "image": "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0",
                "subcategories": [
                    "Tennis Rackets",
                    "Tennis Balls",
                    "Tennis Shoes",
                    "Tennis Clothing",
                    "Racket Grips",
                    "Racket Strings",
                    "Tennis Bags",
                    "Accessories",
                ],
            },

            "Table Tennis": {
                "image": "https://images.unsplash.com/photo-1534158914592-062992fbe900",
                "subcategories": [
                    "Table Tennis Tables",
                    "TT Rackets",
                    "Table Tennis Balls",
                    "Rubber & Blades",
                    "Nets",
                    "Shoes",
                    "Accessories",
                ],
            },

            "Running & Athletics": {
                "image": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5",
                "subcategories": [
                    "Running Shoes",
                    "Running Clothes",
                    "Running Shorts",
                    "Track Shoes",
                    "Socks",
                    "Running Accessories",
                    "Fitness Trackers",
                ],
            },

            "Fitness & Gym": {
                "image": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48",
                "subcategories": [
                    "Dumbbells",
                    "Barbells & Weight Plates",
                    "Resistance Bands",
                    "Kettlebells",
                    "Yoga Mats",
                    "Exercise Benches",
                    "Skipping Ropes",
                    "Gym Gloves",
                    "Gym Bags",
                    "Fitness Accessories",
                ],
            },

            "Swimming": {
                "image": "https://images.unsplash.com/photo-1530549387789-4c1017266635",
                "subcategories": [
                    "Swimwear",
                    "Swimming Goggles",
                    "Swimming Caps",
                    "Training Equipment",
                    "Swimming Bags",
                    "Accessories",
                ],
            },

            "Boxing & Martial Arts": {
                "image": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed",
                "subcategories": [
                    "Boxing Gloves",
                    "Punching Bags",
                    "Hand Wraps",
                    "Head Guards",
                    "Shin Guards",
                    "Training Pads",
                    "Martial Arts Uniforms",
                    "Protective Gear",
                ],
            },

            "Outdoor & Adventure": {
                "image": "https://images.unsplash.com/photo-1551632811-561732d1e306",
                "subcategories": [
                    "Cycling",
                    "Skateboards",
                    "Camping Gear",
                    "Hiking Gear",
                    "Sports Sunglasses",
                    "Outdoor Accessories",
                ],
            },

            "Sports Clothing": {
                "image": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438",
                "subcategories": [
                    "Jerseys",
                    "T-Shirts",
                    "Shorts",
                    "Track Pants",
                    "Tracksuits",
                    "Jackets",
                    "Sports Bras",
                    "Socks",
                    "Caps",
                ],
            },

            "Sports Footwear": {
                "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
                "subcategories": [
                    "Cricket Shoes",
                    "Football Shoes",
                    "Running Shoes",
                    "Basketball Shoes",
                    "Badminton Shoes",
                    "Tennis Shoes",
                    "Training Shoes",
                    "Hiking Shoes",
                ],
            },

            "Sports Bags & Accessories": {
                "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62",
                "subcategories": [
                    "Backpacks",
                    "Kit Bags",
                    "Duffel Bags",
                    "Water Bottles",
                    "Towels",
                    "Sports Watches",
                    "Caps",
                    "Sunglasses",
                    "Knee/Elbow Supports",
                    "Other Accessories",
                ],
            },

            "Sports Equipment": {
                "image": "https://images.unsplash.com/photo-1518611012118-696072aa579a",
                "subcategories": [
                    "Cones",
                    "Training Ladders",
                    "Agility Equipment",
                    "Whistles",
                    "Stopwatches",
                    "Training Hurdles",
                    "Goal Posts",
                    "Nets",
                    "Coaching Equipment",
                ],
            },
        }

        created_main = 0
        created_sub = 0

        for main_name, data in categories.items():

            # Create / update main category
            main_category, created = Category.objects.get_or_create(
                name=main_name,
                defaults={
                    "slug": slugify(main_name),
                    "image": data["image"],
                    "parent": None,
                }
            )

            if created:
                created_main += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created: {main_name}")
                )
            else:
                main_category.slug = slugify(main_name)
                main_category.image = data["image"]
                main_category.parent = None
                main_category.save()

            # Create subcategories
            for sub_name in data["subcategories"]:

                # Because Category.name is unique,
                # repeated names such as "Jerseys" and "Accessories"
                # need a unique name.

                existing = Category.objects.filter(
                    name=sub_name
                ).first()

                if existing is None:

                    subcategory = Category.objects.create(
                        name=sub_name,
                        slug=slugify(f"{main_name}-{sub_name}"),
                        parent=main_category,
                    )

                    created_sub += 1

                    self.stdout.write(
                        f"  └── Created: {sub_name}"
                    )

                elif existing.parent_id == main_category.id:

                    # Already belongs to this category
                    existing.slug = slugify(
                        f"{main_name}-{sub_name}"
                    )
                    existing.parent = main_category
                    existing.save()

                else:

                    # Same name already belongs to another category.
                    # Create a unique name using the main category.
                    unique_name = f"{main_name} {sub_name}"

                    subcategory, was_created = Category.objects.get_or_create(
                        name=unique_name,
                        defaults={
                            "slug": slugify(
                                f"{main_name}-{sub_name}"
                            ),
                            "parent": main_category,
                        }
                    )

                    if was_created:
                        created_sub += 1

                        self.stdout.write(
                            f"  └── Created: {unique_name}"
                        )
                    else:
                        subcategory.slug = slugify(
                            f"{main_name}-{sub_name}"
                        )
                        subcategory.parent = main_category
                        subcategory.save()

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Created {created_main} main categories "
                f"and {created_sub} subcategories."
            )
        )