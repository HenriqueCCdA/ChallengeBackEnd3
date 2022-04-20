import csv
from datetime import datetime
from decimal import Decimal
from io import StringIO

from cbe3.core.models import Register, Transaction


def file_csv(file_in_memory):

    f = StringIO(file_in_memory.read().decode('utf-8'))

    transactions = [line for line in csv.reader(f)]

    return transactions


def file_is_empty(transactions):
    return transactions == []


def get_date(transation):
    return datetime.fromisoformat(transation[-1]).date()


def first_date(transactions):
    return get_date(transactions[0])


def transaction_valid_by_date(transactions):
    base_date = first_date(transactions)

    valid = [True]

    for t in transactions[1:]:
        date = get_date(t)

        if date == base_date:
            valid.append(True)
        else:
            valid.append(False)

    return valid


def transaction_valid_by_missing_information(transactions):

    valid = []

    for t in transactions:
        if all(t):
            valid.append(True)

        else:
            valid.append(False)

    return valid


def transaction_valid(transactions):

    valid = transaction_valid_by_missing_information(transactions)
    transactions = [t for t, v in zip(transactions, valid) if v]

    valid = transaction_valid_by_date(transactions)
    transactions = [t for t, v in zip(transactions, valid) if v]

    return transactions


def duplicate_day_transaction(raw_transactions):
    date = first_date(raw_transactions)

    t = Transaction.objects.filter(transaction_datetime__date=date)

    return not len(t) == 0


def list_to_obj(raw_transaction):
    return Transaction(
        source_bank=raw_transaction[0],
        origin_agency=raw_transaction[1],
        origin_account=raw_transaction[2],
        destination_bank=raw_transaction[3],
        destination_agency=raw_transaction[4],
        destination_account=raw_transaction[5],
        transaction_amount=Decimal(raw_transaction[6]),
        transaction_datetime=datetime.fromisoformat(raw_transaction[7])
    )


def save_transactions_db(raw_transactions):
    if not duplicate_day_transaction(raw_transactions):
        date = first_date(raw_transactions)
        Register.objects.create(date=date)
        for t in raw_transactions:
            transaction = list_to_obj(t)
            transaction.save()
        return True
    return False
