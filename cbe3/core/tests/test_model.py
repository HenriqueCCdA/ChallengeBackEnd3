from datetime import datetime
from decimal import Decimal

import pytest
from cbe3.core.models import Transaction
from cbe3.core.transaction import duplicate_day_transaction, list_to_obj, save_transactions_db


@pytest.fixture
def transaction(db):
    transaction = Transaction(
        source_bank='BANCO DO BRASIL',
        origin_agency='0001',
        origin_account='00001-1',
        destination_bank='BANCO BRADESCO',
        destination_agency='0001',
        destination_account='00001-1',
        transaction_amount=Decimal('8000.00'),
        transaction_datetime=datetime.fromisoformat('2022-01-01T07:30:00')
    )

    return transaction


@pytest.fixture
def raw_transactions():
    return (['BANCO DO BRASIL', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '8000', '2022-01-01T07:30:00'],
            ['BANCO SANTANDER', '0001', '00001-1', 'BANCO BRADESCO', '0001', '00001-1', '210', '2022-01-01T08:12:00'])


def test_save_model(transaction):
    transaction.save()
    assert Transaction.objects.exists()


def test_list_to_obj(raw_transactions):

    raw_transaction = raw_transactions[0]
    transaction = list_to_obj(raw_transaction)

    assert transaction.source_bank == raw_transaction[0]
    assert transaction.origin_agency == raw_transaction[1]
    assert transaction.origin_account == raw_transaction[2]
    assert transaction.destination_bank == raw_transaction[3]
    assert transaction.destination_agency == raw_transaction[4]
    assert transaction.destination_account == raw_transaction[5]
    assert transaction.transaction_amount == Decimal(raw_transaction[6])
    assert transaction.transaction_datetime == datetime.fromisoformat(raw_transaction[7])


def test_duplicate_day_transaction(transaction, raw_transactions):
    transaction.save()
    assert duplicate_day_transaction(raw_transactions)


def test_not_save_duplicate_transaction(raw_transactions, db):

    assert save_transactions_db(raw_transactions)

    assert not save_transactions_db(raw_transactions)

    qs = Transaction.objects.all()

    assert len(qs) == 2
