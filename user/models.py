from django.db import models
import uuid

class User(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
