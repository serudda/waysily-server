from django.db import models

class Early(models.Model):
    """ Early Adopter Model """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

