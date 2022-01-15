import uuid
from django.db import models

# Create your models here.


class KeyGen(models.Model):
    id = models.UUIDField(
        editable=False, default=uuid.uuid4, primary_key=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)