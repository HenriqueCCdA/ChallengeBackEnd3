from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from cbe3.core.transaction import file_is_empty, first_date, read_csv, save_transactions_db, transaction_valid


def import_csv(request):

    if request.method == 'POST' and request.FILES['csv-file']:
        csv_file = request.FILES['csv-file']
        fs = FileSystemStorage()
        file_name = fs.save(csv_file.name, csv_file)
        path_file_name = fs.path(file_name)
        raw_transactions = read_csv(file_path=path_file_name)
        raw_transactions = transaction_valid(raw_transactions)

        if file_is_empty(raw_transactions):
            return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'empty'})

        if not save_transactions_db(raw_transactions):
            return render(request, 'import_csv.html', {'csv_file': csv_file,
                                                       'status': 'duplicate',
                                                       'day': first_date(raw_transactions)})

        return render(request, 'import_csv.html', {'csv_file': csv_file, 'status': 'ok'})

    return render(request, 'import_csv.html')
