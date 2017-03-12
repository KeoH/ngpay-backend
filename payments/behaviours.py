
from django.conf import settings
from django.db import models

class TimestampBehaviour(models.Model):

    creation_date = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)

    class Meta:
        abstract = True
