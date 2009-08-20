from django.contrib import admin

from experience.models import ExperienceType, ExperienceItem, LineItem

class ExperienceItemInline(admin.TabularInline):
    model = ExperienceItem

class LineItemInline(admin.TabularInline):
    model = LineItem

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        LineItemInline
    ]

admin.site.register(ExperienceType)
admin.site.register(ExperienceItem, ExperienceAdmin)
