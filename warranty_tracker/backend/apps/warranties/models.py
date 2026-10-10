
from mongoengine import Document, ReferenceField, StringField, DateTimeField, IntField
from apps.products.models import Product
from datetime import datetime

class Warranty(Document):
    product_id = ReferenceField(Product, required=True)
    warranty_type = StringField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    duration = IntField()
    coverage = StringField()
    document_id = StringField()
    reminder_status = StringField(default="NONE")
    created_at = DateTimeField(default=datetime.utcnow)
