from django.db import models

class Admin(models.Model):
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    class Meta:
        db_table = 'admin_signup'

class User(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    class Meta:
        db_table = 'user_signup'

class Contact(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    message = models.TextField(max_length=50)

    class Meta:
        db_table = 'contact_us'
