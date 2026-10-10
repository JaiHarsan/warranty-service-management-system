
from mongoengine import Document, StringField, FloatField, ListField

class ServiceCentre(Document):
    brand = StringField()
    name = StringField()
    city = StringField()
    latitude = FloatField()
    longitude = FloatField()
    services = ListField(StringField())
