from cbe3.core.tests.conftest import transaction_from_file
from cbe3.core.transaction import (first_date,
                                   transaction_valid,
                                   transaction_valid_by_date,
                                   transaction_valid_by_missing_information)


def test_file_csv_first_date(csv_all_valid):
    t = transaction_from_file(csv_all_valid)

    date = first_date(t)

    assert '2022-01-01' == str(date)


def test_all_transaction_valid_by_date(csv_all_valid):

    t = transaction_from_file(csv_all_valid)

    valid = transaction_valid_by_date(t)

    assert valid == [True, True, True]


def test_transaction_invalid_by_day(csv_invalid_by_day):

    t = transaction_from_file(csv_invalid_by_day)

    valid = transaction_valid_by_date(t)

    assert valid == [True, False, True]


def test_transaction_invalid_by_month(csv_invalid_by_month):

    t = transaction_from_file(csv_invalid_by_month)

    valid = transaction_valid_by_date(t)

    assert valid == [True, True, False]


def test_transaction_invalid_by_year(csv_invalid_by_year):

    t = transaction_from_file(csv_invalid_by_year)

    valid = transaction_valid_by_date(t)

    assert valid == [True, False, True]


def test_transaction_invalid_by_missing_information(csv_miss_info):

    t = transaction_from_file(csv_miss_info)

    valid = transaction_valid_by_missing_information(t)

    assert valid == [True, False, True]


def test_transaction_first_miss_info(csv_first_miss_info):

    t = transaction_from_file(csv_first_miss_info)

    t_valid = transaction_valid(t)

    expected = [
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
    ]

    assert t_valid == expected


def test_transaction_real_exemplo(csv_real_exemplo):

    t = transaction_from_file(csv_real_exemplo)

    t_valid = transaction_valid(t)

    expected = [
        ['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
        ['BANCO BANRISUL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '100', '2022-01-01T16:30:00'],
        ['BANCO ITAU', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '1000', '2022-01-01T19:30:00'],
        ['NUBANK', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '2000', '2022-01-01T19:34:00'],
    ]

    assert len(t_valid) == len(expected)
