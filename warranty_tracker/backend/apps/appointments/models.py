
from mongoengine import Document, ReferenceField, StringField, DateTimeField
from apps.accounts.models import User
from apps.products.models import Product
from apps.service_centres.models import ServiceCentre
from datetime import datetime

class Appointment(Document):
    user_id = ReferenceField(User, required=True)
    product_id = ReferenceField(Product, required=True)
    service_centre_id = ReferenceField(ServiceCentre, required=True)
    issue = StringField()
    date = StringField()
    time = StringField()
    status = StringField(default="REQUESTED")
    request_id = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
