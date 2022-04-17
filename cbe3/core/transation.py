from datetime import datetime


def read_csv(file_path=None):
    import csv

    transactions = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for r in reader:
            transactions.append(r)

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


def transcation_save_db(transactions):
    pass