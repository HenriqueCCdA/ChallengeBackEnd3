from http import HTTPStatus

from django.test import Client


def test_status_code_home(client: Client):
    resp = client.get('/')

    assert resp.status_code == HTTPStatus.OK
