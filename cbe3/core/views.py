from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from cbe3.core.transation import file_is_empty, read_csv


def import_csv(request):

    if request.method == 'POST' and request.FILES['csv-file']:
        csv_file = request.FILES['csv-file']
        fs = FileSystemStorage()
        file_name = fs.save(csv_file.name, csv_file)
        path_file_name = fs.path(file_name)
        list_ = read_csv(file_path=path_file_name)

        if file_is_empty(list_):
            return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'empty'})

        return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'ok'})


    return render(request, 'import_csv.html')
