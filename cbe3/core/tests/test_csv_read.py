from cbe3.core.transaction import (file_is_empty,
                                   first_date,
                                   transaction_valid,
                                   transaction_valid_by_date,
                                   transaction_valid_by_missing_information)
from cbe3.core.views import read_csv
from unittest import mock


def test_csv_read_exist_file(mocker, csv_all_valid):

    mock_open = mock.mock_open(read_data=csv_all_valid)

    mocker.patch('builtins.open', mock_open)

    list_ = read_csv()

    expected = [
        ['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
    ]

    assert list_ == expected


def test_csv_empty(mocker):
    mock_open = mock.mock_open(read_data='')

    mocker.patch('builtins.open', mock_open)

    list_ = read_csv()

    assert file_is_empty(list_)


def test_read_first_date(mocker, csv_all_valid):

    mock_open = mock.mock_open(read_data=csv_all_valid)

    mocker.patch('builtins.open', mock_open)

    date = first_date(read_csv())

    assert '2022-01-01' == str(date)


def test_all_transaction_valid_by_date(mocker, csv_all_valid):

    mock_open = mock.mock_open(read_data=csv_all_valid)

    mocker.patch('builtins.open', mock_open)

    valid = transaction_valid_by_date(read_csv())

    assert valid == [True, True, True]


def test_transaction_invalid_by_day(mocker, csv_invalid_by_day):

    mock_open = mock.mock_open(read_data=csv_invalid_by_day)

    mocker.patch('builtins.open', mock_open)

    valid = transaction_valid_by_date(read_csv())

    assert valid == [True, False, True]


def test_transaction_invalid_by_month(mocker, csv_invalid_by_month):

    mock_open = mock.mock_open(read_data=csv_invalid_by_month)

    mocker.patch('builtins.open', mock_open)

    valid = transaction_valid_by_date(read_csv())

    assert valid == [True, True, False]


def test_transaction_invalid_by_year(mocker, csv_invalid_by_year):

    mock_open = mock.mock_open(read_data=csv_invalid_by_year)

    mocker.patch('builtins.open', mock_open)

    valid = transaction_valid_by_date(read_csv())

    assert valid == [True, False, True]


def test_transaction_invalid_by_missing_information(mocker, csv_miss_info):

    mock_open = mock.mock_open(read_data=csv_miss_info)

    mocker.patch('builtins.open', mock_open)

    valid = transaction_valid_by_missing_information(read_csv())

    assert valid == [True, False, True]


def test_transaction_first_miss_info(mocker, csv_first_miss_info):

    mock_open = mock.mock_open(read_data=csv_first_miss_info)

    mocker.patch('builtins.open', mock_open)

    t = read_csv()

    t_valid = transaction_valid(t)

    expected = [
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
    ]

    assert t_valid == expected


def test_transaction_real_exemplo(mocker, csv_real_exemplo):

    mock_open = mock.mock_open(read_data=csv_real_exemplo)

    mocker.patch('builtins.open', mock_open)

    t = read_csv()

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
