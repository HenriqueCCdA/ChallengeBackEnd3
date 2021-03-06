from io import BytesIO

import pytest
from cbe3.core.models import User
from cbe3.core.transaction import file_csv
from django.core.files.uploadedfile import InMemoryUploadedFile


DATE1 = '2022-01-01T07:30:00'
DATE2 = '2022-01-01T08:12:00'
DATE3 = '2022-01-01T08:44:00'

DAY_WRONG = '2022-01-02T08:12:00'
MONTH_WRONG = '2022-02-01T08:12:00'
YEAR_WRONG = '2023-01-01T08:12:00'


@pytest.fixture
def csv_all_valid():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,{DATE2}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{DATE3}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_invalid_by_day():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,{DAY_WRONG}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{DATE3}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_invalid_by_month():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,{DATE2}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{MONTH_WRONG}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_invalid_by_year():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,{YEAR_WRONG}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{DATE3}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_miss_info():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,,210,{DATE2}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{DATE3}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_first_miss_info():
    line1 = f'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,,{DATE1}'
    line2 = f'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,{DATE2}'
    line3 = f'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,{DATE3}'

    return '\n'.join((line1, line2, line3))


@pytest.fixture
def csv_real_exemplo():
    line1 = 'BANCO DO BRASIL,0001,00001-1,BANCO BRADESCO,0001,00001-1,8000,2022-01-01T07:30:00'
    line2 = 'BANCO SANTANDER,0001,00001-1,BANCO BRADESCO,0001,00001-1,210,2022-01-01T08:12:00'
    line3 = 'BANCO SANTANDER,0001,00002-1,BANCO BRADESCO,0001,00001-1,79800.22,2022-01-01T08:44:00'
    line4 = 'BANCO BRADESCO,0001,00001-1,BANCO SANTANDER,0001,00002-1,,2022-01-01T12:32:00'
    line5 = 'BANCO BANRISUL,0001,00001-1,BANCO BRADESCO,0001,00001-1,100,2022-01-01T16:30:00'
    line6 = 'BANCO ITAU,0001,00001-1,BANCO BRADESCO,0001,00001-1,19000.50,2022-01-03T16:55:00'
    line7 = 'BANCO ITAU,0001,00002-1,BANCO BRADESCO,0001,00001-1,1000,2022-01-01T19:30:00'
    line8 = 'NUBANK,0001,00001-1,BANCO BRADESCO,0001,00001-1,2000,2022-01-01T19:34:00'
    line9 = 'BANCO INTER,0001,00001-1,BANCO BRADESCO,0001,00001-1,300,2022-01-09T20:30:00'
    line10 = 'CAIXA ECONOMICA FEDERAL,0001,00001-1,BANCO BRADESCO,0001,,900,2022-01-01T22:30:00'

    return '\n'.join((line1, line2, line3, line4, line5, line6, line7, line8, line9, line10))


def transaction_from_file(csv_str_format):
    file = BytesIO(csv_str_format.encode())
    size = file.getbuffer().nbytes
    file_in_memory = InMemoryUploadedFile(file,
                                          'test_file.csv',
                                          'text/csv',
                                          size,
                                          None,
                                          {})
    return file_csv(file_in_memory)


@pytest.fixture
def users(db):
    user1 = User.objects.create(username='Rodrigo da Silva',
                                email='rodrigo.silva@email.com',
                                is_staff='False')
    user2 = User.objects.create(username='Jacqueline Oliveira',
                                email='jacqueline.oliveira@email.com.br',
                                is_staff='False')

    return user1, user2
