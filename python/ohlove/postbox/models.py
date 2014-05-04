from django.db import models
from mongoengine import *
# Create your models here.

class post(Document):
	content = StringField(required=True)
	datetime = DateTimeField(required=True)
	weekday = StringField(required=True,max_length=20)