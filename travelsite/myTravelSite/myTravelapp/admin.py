from django.contrib import admin

# Register your models here.
from .models import tourPics, teamPics

admin.site.register(tourPics)
admin.site.register(teamPics)
