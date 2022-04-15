from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def read_csv(file_path=None):
    import csv

    transations = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for r in reader:
            transations.append(r)

    return transations


def import_csv(request):

    if request.method == 'POST' and request.FILES['csv-file']:
        csv_file = request.FILES['csv-file']
        fs = FileSystemStorage()
        file_name = fs.save(csv_file.name, csv_file)
        path_file_name = fs.path(file_name)
        try:
            list_ = read_csv(file_path=path_file_name)
            print(list_)
            return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'ok'})
        except FileNotFoundError:
            return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'fail'})

    return render(request, 'import_csv.html')
