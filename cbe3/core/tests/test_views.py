from http import HTTPStatus

from django.test import Client

from cbe3.core.django_assertions import assert_template_use


def test_read_csv_file(client: Client):
    resp = client.get('/import/')

    assert resp.status_code == HTTPStatus.OK


def test_template_import_csv_file(client: Client):
    resp = client.get('/import/')

    assert_template_use(response=resp, template_name='import_csv.html')
