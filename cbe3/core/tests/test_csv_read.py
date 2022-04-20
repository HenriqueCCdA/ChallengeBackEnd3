from cbe3.core.tests.conftest import transaction_from_file
from cbe3.core.transaction import file_is_empty


def test_file_csv(csv_all_valid):

    t = transaction_from_file(csv_all_valid)

    expected = [
        ['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
    ]

    assert t == expected


def test_csv_empty():

    t = transaction_from_file('')

    assert file_is_empty(t)
