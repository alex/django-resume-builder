from django.contrib.localflavor.us.models import USStateField
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField()

    def __unicode__(self):
        return self.full_name

class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = USStateField()
    zipcode = models.CharField(max_length=5)

    person = models.OneToOneField(Person, null=True)

    def __unicode__(self):
        return self.street
