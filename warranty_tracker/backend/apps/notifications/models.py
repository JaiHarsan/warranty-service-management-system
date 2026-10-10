
from mongoengine import Document, ReferenceField, StringField, DateTimeField, BooleanField
from apps.accounts.models import User
from datetime import datetime

class Notification(Document):
    user_id = ReferenceField(User, required=True)
    type = StringField()
    title = StringField()
    message = StringField()
    read = BooleanField(default=False)
    related_product_id = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
