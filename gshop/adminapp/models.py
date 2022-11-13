from django.db import models

class Grocery(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.TextField(max_length=100)
    image = models.CharField(max_length=150)

    class Meta:
        db_table = 'grocery'

class Medicine(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.TextField(max_length=100)
    image = models.TextField(max_length=150)

    class Meta:
        db_table = 'medicine'

