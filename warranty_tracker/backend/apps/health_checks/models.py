
from mongoengine import Document, ReferenceField, DictField, StringField, DateTimeField
from apps.products.models import Product
from datetime import datetime

class HealthCheck(Document):
    product_id = ReferenceField(Product, required=True)
    responses = DictField()
    symptoms = StringField()
    risk_level = StringField()
    potential_issue = StringField()
    recommendation = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
