
from mongoengine import Document, StringField, FloatField, DateTimeField, ReferenceField
from apps.accounts.models import User
from datetime import datetime

class Product(Document):
    user_id = ReferenceField(User, required=True)
    brand = StringField(required=True)
    category = StringField(required=True)
    product_name = StringField(required=True)
    model_number = StringField()
    serial_number = StringField()
    purchase_date = DateTimeField()
    purchase_price = FloatField()
    warranty_start = DateTimeField()
    warranty_end = DateTimeField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
