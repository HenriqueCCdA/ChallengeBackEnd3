from http import HTTPStatus
from django.shortcuts import resolve_url
import pytest
from cbe3.core.django_assertions import assert_template_use, assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(resolve_url('users_list'))


def test_list_user_status_code(resp):
    assert resp.status_code == HTTPStatus.OK


def test_list_user_template(resp):
    assert_template_use(resp, 'users_list.html')


def test_table_columns(resp):
    assert_contains(resp, '<table')
    assert_contains(resp, '<th scope="col">ID</th>')
    assert_contains(resp, '<th scope="col">EMAIL</th>')
    assert_contains(resp, '<th scope="col">NOME</th>')
    assert_contains(resp, '<th scope="col">OPÇÕES</th>')


def test_list_of_users(client, users):
    resp = client.get(resolve_url('users_list'))
    for u in users:
        assert_contains(resp, u.username)
        assert_contains(resp, u.email)
