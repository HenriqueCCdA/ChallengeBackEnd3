from cbe3.core.views import read_csv


def test_csv_read_exist_file():
    list_ = read_csv(file_path='contrib/transacoes-2022-01-01.csv')

    expected = [
        ['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
        ['BANCO BRADESCO', '0001', '00001-1', 'BANCO SANTANDER', '0001', '00002-1', '11.50', '2022-01-01T12:32:00'],
        ['BANCO BANRISUL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '100', '2022-01-01T16:30:00'],
        ['BANCO ITAU', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '19000.50', '2022-01-01T16:55:00'],
        ['BANCO ITAU', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '1000', '2022-01-01T19:30:00'],
        ['NUBANK', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '2000', '2022-01-01T19:34:00'],
        ['BANCO INTER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '300', '2022-01-01T20:30:00'],
        ['CAIXA ECONOMICA FEDERAL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '900', '2022-01-01T22:30:00']
    ]
    assert len(list_) == 10
    assert list_ == expected


# def test_csv_read_not_exist_file():

#     list_ = read_csv(file_path='contrib/transacoes-2022-01-01.cs')

#     assert list_ == None
