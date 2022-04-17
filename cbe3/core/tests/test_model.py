from datetime import datetime
from decimal import Decimal

import pytest
from cbe3.core.models import Transaction


@pytest.fixture
def create_trasaction(db):
    transaction = Transaction(
        source_bank = 'BANCO DO BRASIL',
        origin_agency = '0001',
        origin_account = '00001-1',
        destination_bank = 'BANCO BRADESCO',
        destination_agency = '0001',
        destination_account = '00001-1',
        transaction_amount = Decimal('8000.00'),
        transaction_datetime = datetime.fromisoformat('2022-01-01T07:30:00')
    )

    transaction.save()


def test_model(create_trasaction):
    assert Transaction.objects.exists()
