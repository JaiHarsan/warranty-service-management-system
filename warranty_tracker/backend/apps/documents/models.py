
from mongoengine import Document, ReferenceField, StringField, DateTimeField, IntField
from apps.accounts.models import User
from apps.products.models import Product
from datetime import datetime

class DocumentItem(Document):
    user_id = ReferenceField(User, required=True)
    product_id = ReferenceField(Product)
    document_type = StringField()
    filename = StringField()
    storage_path = StringField()
    mime_type = StringField()
    size = IntField()
    created_at = DateTimeField(default=datetime.utcnow)

