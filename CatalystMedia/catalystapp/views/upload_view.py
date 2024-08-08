from django.shortcuts import redirect, render
from ..models.file import FileUploader, CsvData
import pandas as pd
from django.db.models import Count

def create_data_from_csv(filepath):
    df = pd.read_csv(filepath, delimiter=',')
    df = df.where(pd.notnull(df), None) 
    
    list_of_csv_rows = df.values.tolist()

    for list_of_data in list_of_csv_rows:
        year_founded = list_of_data[3]
        if year_founded is not None:
            try:
                year_founded = int(year_founded)
            except ValueError:
                year_founded = None
        CsvData.objects.create(
            company_number = list_of_data[0] if list_of_data[0] is not None else 'Unknown',
            name = list_of_data[1] if list_of_data[1] is not None else 'Unknown',
            domain = list_of_data[2] if list_of_data[2] is not None else 'example.com',
            year_founded = year_founded,
            industry = list_of_data[4] if list_of_data[4] is not None else 'Unknown',
            size_range = list_of_data[5] if list_of_data[5] is not None else 'Unknown',
            locality = list_of_data[6] if list_of_data[6] is not None else 'Unknown',
            country = list_of_data[7] if list_of_data[7] is not None else 'Unknown',
            linkedin_url = list_of_data[8] if list_of_data[8] is not None else 'Unknown',
            current_employee_estimate = list_of_data[9],
            total_employee_estimate = list_of_data[10],
        )

def upload_view(request):
    if request.method == "POST":
        file = request.FILES['files']
        file_obj = FileUploader.objects.create(file=file)
        create_data_from_csv(file_obj.file)
        data_count = CsvData.objects.all().aggregate(Count('name'))
        count = data_count['name__count']
        return render(request, 'upload.html', {'data_count':count})
    return render(request, 'upload.html')