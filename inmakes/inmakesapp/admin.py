from django.contrib import admin

# Register your models here.
from . models import place,icon
admin.site.register(place)
admin.site.register(icon)