
from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime
import uuid

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField()
    password_hash = StringField(required=True)
    token = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
