# SPORTIVA — Django Sports Retail E-Commerce

A functional Django + Django Templates sports retail application. Bootstrap 5 and Chart.js are loaded from CDNs. Product demo imagery uses remote Unsplash image URLs; uploaded product images are supported through `ImageField`.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```
Open http://127.0.0.1:8000/

Demo admin: `admin` / `Admin123!`
Demo customer: `customer1` / `Sportiva123!`

## Production
Set `DJANGO_SECRET_KEY`, `DEBUG=False`, and `DATABASE_URL` for PostgreSQL. Run `python manage.py collectstatic` and serve the project with Gunicorn/your preferred WSGI host. Configure persistent `MEDIA_ROOT` storage for uploaded product images.

## Included
Home, category browsing, search/sort/pagination, product pages, authentication, password reset routes, cart, checkout, orders/tracking, wishlist, dashboard, support requests, maintenance reminders model, campaigns/segmentation models, customer/profile model, inventory, Django admin, Chart.js reporting dashboard, seed data, responsive Bootstrap UI.
