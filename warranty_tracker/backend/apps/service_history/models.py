
from mongoengine import Document, ReferenceField, StringField, DateTimeField, FloatField, ListField
from apps.products.models import Product
from datetime import datetime

class ServiceHistory(Document):
    product_id = ReferenceField(Product, required=True)
    appointment_id = StringField()
    issue = StringField()
    diagnosis = StringField()
    repair = StringField()
    parts_replaced = StringField()
    service_date = DateTimeField()
    cost = FloatField()
    notes = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
