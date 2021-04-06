from django.contrib import admin
from .models import Webapp

class WebappAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Webapp, WebappAdmin)