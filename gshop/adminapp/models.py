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

class Orders(models.Model):
   product_name = models.TextField(max_length=100) 
   product_quantity = models.TextField(max_length=100)
   name = models.TextField(max_length=50)
   phone = models.TextField(max_length=50)
   address = models.TextField(max_length=50)

   class Meta:
    db_table = 'orders'


class Message(models.Model):
    message = models.TextField(max_length= 250)

    class Meta:
        db_table = 'message'

