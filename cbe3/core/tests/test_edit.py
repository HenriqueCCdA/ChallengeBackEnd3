from http import HTTPStatus
from django.shortcuts import resolve_url
import pytest
from cbe3.core.django_assertions import assert_template_use


@pytest.fixture
def resp(client, users):
    return client.get(resolve_url('update_user', id=1))


def test_update_user_status_code(resp):
    assert resp.status_code == HTTPStatus.OK


def test_update_user_template(resp):
    assert_template_use(resp, 'edit_user.html')
