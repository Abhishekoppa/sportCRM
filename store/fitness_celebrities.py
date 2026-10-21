"""Local portraits for male fitness celebrities and athletes (saved locally in static folder)."""

FITNESS_CELEBRITIES = [
    {
        "name": "Virat Kohli",
        "role": "Cricket & Fitness Legend",
        "image": "/static/store/images/celebrities/virat_kohli.jpg",
        "quote": "Discipline and training make the champion.",
    },
    {
        "name": "Cristiano Ronaldo",
        "role": "Football & Training Icon",
        "image": "/static/store/images/celebrities/cristiano_ronaldo.jpg",
        "quote": "Dedication, hard work, and belief in every session.",
    },
    {
        "name": "Vidyut Jammwal",
        "role": "Action & Martial Arts Pro",
        "image": "/static/store/images/celebrities/vidyut_jammwal.jpg",
        "quote": "True strength comes from endurance and agility.",
    },
    {
        "name": "Arnold Schwarzenegger",
        "role": "Bodybuilding Legend",
        "image": "/static/store/images/celebrities/arnold_schwarzenegger.jpg",
        "quote": "No pain, no gain. Conquer your goals.",
    },
    {
        "name": "Dwayne Johnson",
        "role": "Strength & Conditioning Beast",
        "image": "/static/store/images/celebrities/dwayne_johnson.jpg",
        "quote": "Blood, sweat and respect. First two you give, last one you earn.",
    },
    {
        "name": "Rafael Nadal",
        "role": "Tennis & Endurance Legend",
        "image": "/static/store/images/celebrities/rafael_nadal.jpg",
        "quote": "Endure and conquer every point through relentless focus.",
    },
    {
        "name": "Hrithik Roshan",
        "role": "Bollywood Fitness Icon",
        "image": "/static/store/images/celebrities/hrithik_roshan.jpg",
        "quote": "Transform your limits every single day.",
    },
    {
        "name": "LeBron James",
        "role": "Basketball Performance Great",
        "image": "/static/store/images/celebrities/lebron_james.jpg",
        "quote": "Strive for greatness in every drill and every game.",
    },
    {
        "name": "Neeraj Chopra",
        "role": "Olympic Gold & Track Power",
        "image": "/static/store/images/celebrities/neeraj_chopra.jpg",
        "quote": "Give 100% in your training, success will follow.",
    },
    {
        "name": "Lionel Messi",
        "role": "Football & Speed Legend",
        "image": "/static/store/images/celebrities/lionel_messi.jpg",
        "quote": "You have to fight to reach your dream. You have to sacrifice.",
    },
]


def celebrity_image_urls():
    return [c["image"] for c in FITNESS_CELEBRITIES]


def get_celebrity_for_product(product_name):
    """Return male fitness celebrity associated with a product."""
    mapping = {
        "Hydration Pack": FITNESS_CELEBRITIES[2],          # Vidyut Jammwal
        "Golf Clubs": FITNESS_CELEBRITIES[0],              # Virat Kohli
        "Bicycle": FITNESS_CELEBRITIES[1],                 # Cristiano Ronaldo
        "Yoga Mat": FITNESS_CELEBRITIES[6],                # Hrithik Roshan
        "Snowboard": FITNESS_CELEBRITIES[3],               # Arnold Schwarzenegger
        "Tennis Racquet": FITNESS_CELEBRITIES[5],          # Rafael Nadal
        "Basketball Shoes": FITNESS_CELEBRITIES[7],        # LeBron James
        "Treadmill": FITNESS_CELEBRITIES[4],               # Dwayne Johnson
        "Skis": FITNESS_CELEBRITIES[8],                    # Neeraj Chopra
        "Fitness Tracker": FITNESS_CELEBRITIES[1],         # Cristiano Ronaldo
        "Moisture-Wicking Socks": FITNESS_CELEBRITIES[0],    # Virat Kohli
        "Running Shoes": FITNESS_CELEBRITIES[0],           # Virat Kohli
    }
    return mapping.get(product_name, FITNESS_CELEBRITIES[0])
