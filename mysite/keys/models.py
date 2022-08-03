import uuid
from django.db import models


# Create your models here.
class Key(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    active = models.BooleanField(default=True)
    card_id = models.CharField(max_length=20, default=None, db_index=True)

    def __str__(self):
        return f"{self.id}, {self.active}"
