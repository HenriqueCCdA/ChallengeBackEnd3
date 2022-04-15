import pytest
from cbe3.core.views import read_csv
from unittest import mock


@pytest.fixture
def csv_file():
    line1 = 'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,2022-01-01T07:30:00'
    line2 = 'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,2022-01-01T08:12:00'
    line3 = 'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,2022-01-01T08:44:00'

    return '\n'.join((line1, line2, line3))


def test_csv_read_exist_file(mocker, csv_file):

    mock_open = mock.mock_open(read_data=csv_file)

    mocker.patch('builtins.open', mock_open)

    list_ = read_csv()

    expected = [
        ['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
        ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'],
        ['BANCO SANTANDER', '0001', '00002-1', 'BANCO BRADESCO', '0001', '00001-1', '79800.22', '2022-01-01T08:44:00'],
    ]
    assert len(list_) == 3
    assert list_ == expected


# def test_csv_read_not_exist_file():

#     list_ = read_csv(file_path='contrib/transacoes-2022-01-01.cs')

#     assert list_ == None
