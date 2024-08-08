from django.contrib import admin
from .models.file import CsvData

# Register your models here.
class CsvDataAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(CsvData, CsvDataAdmin)