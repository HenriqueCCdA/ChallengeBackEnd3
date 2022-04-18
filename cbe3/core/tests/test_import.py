from unittest import mock
from cbe3.core.models import Register
from cbe3.core.transaction import first_date, read_csv, save_transactions_db, transaction_valid


def test_import(mocker, csv_all_valid, db):

    mock_open = mock.mock_open(read_data=csv_all_valid)

    mocker.patch('builtins.open', mock_open)

    t = read_csv()

    t_valid = transaction_valid(t)

    save_transactions_db(t_valid)

    r = Register.objects.all().first()

    assert r.date == first_date(t_valid)
