from django.db import models

class FileUploader(models.Model):
    file = models.FileField(upload_to="files")

class CsvData(models.Model):
    company_number = models.IntegerField()
    name = models.CharField(max_length=120)
    domain = models.CharField(max_length=120)
    year_founded = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=120)
    size_range = models.CharField(max_length=120)
    locality = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    linkedin_url = models.CharField(max_length=250)
    current_employee_estimate = models.IntegerField(null=True, blank=True)
    total_employee_estimate = models.IntegerField(null=True, blank=True)