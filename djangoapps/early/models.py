import uuid

from django.db import models


class Early(models.Model):
    """ Early Adopter Model """
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100, default='*')
    last_name = models.CharField(max_length=100, default='*')
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=500)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

