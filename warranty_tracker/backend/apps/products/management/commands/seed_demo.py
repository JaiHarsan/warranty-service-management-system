
from django.core.management.base import BaseCommand
from apps.accounts.models import User
from apps.products.models import Product
from apps.service_centres.models import ServiceCentre
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seeds demo data for WarrantyCare'

    def handle(self, *args, **kwargs):
        # User
        password_hash = make_password('demo123')
        user = User.objects(email="rahul@example.com").first()
        if not user:
            user = User(name="Rahul Kumar", email="rahul@example.com", password_hash=password_hash)
            user.save()
            self.stdout.write("Created demo user rahul@example.com / demo123")
        
        # Products
        if Product.objects.count() == 0:
            Product(user_id=user, brand="HP", category="laptop", product_name="Pavilion").save()
            Product(user_id=user, brand="Samsung", category="smartphone", product_name="Galaxy S23").save()
            Product(user_id=user, brand="LG", category="washing_machine", product_name="Smart Washer").save()
            self.stdout.write("Created demo products")
            
        # Service Centres
        if ServiceCentre.objects.count() == 0:
            ServiceCentre(brand="HP", name="HP Authorized SC", city="Coimbatore", latitude=11.0168, longitude=76.9558, services=["Laptop repair"]).save()
            ServiceCentre(brand="Samsung", name="Samsung Care", city="Coimbatore", latitude=11.0180, longitude=76.9600, services=["Mobile repair"]).save()
            self.stdout.write("Created demo service centres")
            
        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
