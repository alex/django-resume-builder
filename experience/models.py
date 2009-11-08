from django.db import models

from people.models import Person

class ExperienceType(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.name

class ExperienceItem(models.Model):
    person = models.ForeignKey(Person, related_name='experiences')
    type = models.ForeignKey(ExperienceType)

    title = models.CharField(max_length=100)

    location = models.CharField(max_length=255, blank=True)
    time_period = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return "%s at %s" % (self.person, self.title)
    
    class Meta:
        ordering = ("type",)

class LineItem(models.Model):
    experience = models.ForeignKey(ExperienceItem, related_name="items")
    details = models.CharField(max_length=255)
