from cbe3.core.models import Register
from cbe3.core.tests.conftest import transaction_from_file
from cbe3.core.transaction import first_date, save_transactions_db, transaction_valid


def test_import(csv_all_valid, db):

    t = transaction_from_file(csv_all_valid)

    t_valid = transaction_valid(t)

    save_transactions_db(t_valid)

    r = Register.objects.all().first()

    assert r.date == first_date(t_valid)
