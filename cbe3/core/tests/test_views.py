from http import HTTPStatus

from django.test import Client


def test_read_csv_file(client: Client):
    resp = client.get('/import/')

    assert resp.status_code == HTTPStatus.OK
