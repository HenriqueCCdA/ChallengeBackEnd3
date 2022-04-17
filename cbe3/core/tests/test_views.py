from http import HTTPStatus
from unittest import mock

from django.test import Client
import pytest

from cbe3.core.django_assertions import assert_template_use, assert_contains


def test_read_csv_file(client: Client):
    resp = client.get('/import/')

    assert resp.status_code == HTTPStatus.OK


def test_template_import_csv_file(client: Client):
    resp = client.get('/import/')

    assert_template_use(response=resp, template_name='import_csv.html')


@pytest.mark.skip
def test_empty_csv(client, mocker, csv_all_valid):

    mock_open = mock.mock_open(read_data=csv_all_valid)

    mocker.patch('builtins.open', mock_open)

    with open('file.csv') as f:
        resp = client.post('/import/', {'csv-file': f})

    assert_contains(resp, '<p>')