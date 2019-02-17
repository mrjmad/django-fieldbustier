from django.db import models


class DummyModel(models.Model):
    char_field = models.CharField(max_length=12)
    int_field = models.PositiveIntegerField(default=2)
    decimal_field = models.DecimalField(default=0, max_digits=14, decimal_places=2)
