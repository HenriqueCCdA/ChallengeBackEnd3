from http import HTTPStatus
from django.shortcuts import resolve_url
import pytest
from cbe3.core.django_assertions import assert_template_use


@pytest.fixture
def url():
    return resolve_url('users_list')


def test_list_user_status_code(client, url, db):
    resp = client.get(url)

    assert resp.status_code == HTTPStatus.OK


def test_list_user_template(client, url, db):
    resp = client.get(url)

    assert_template_use(resp, 'users_list.html')
