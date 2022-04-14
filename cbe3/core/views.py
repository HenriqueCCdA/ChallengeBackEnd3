from django.http import HttpResponse

FILE_CSV = 'contrib/transacoes-2022-01-01.cs'


def read_csv(file_path):
    import csv

    transations = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for r in reader:
            transations.append(r)

    return transations


def import_csv(resquet):

    try:
        read_csv(file_path=FILE_CSV)
        return HttpResponse('Arquivo importado com sucesso')
    except FileNotFoundError:
        return HttpResponse('Falha na importacao do arquivo')
