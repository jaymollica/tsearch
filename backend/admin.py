from django.contrib import admin

# Register your models here.

from backend.models import *

admin.site.register(Artwork)
admin.site.register(Color)
admin.site.register(Country)
admin.site.register(Medium)
