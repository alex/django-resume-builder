from django.contrib import admin

from people.models import Person, Address
from experience.admin import ExperienceItemInline

class AddressInline(admin.TabularInline):
    model = Address

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        ExperienceItemInline
    ]

admin.site.register(Person, PersonAdmin)
