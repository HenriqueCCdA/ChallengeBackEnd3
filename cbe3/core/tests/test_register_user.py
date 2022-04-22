from http import HTTPStatus
from django.shortcuts import resolve_url
from django.test import Client
import pytest
from cbe3.core.django_assertions import assert_template_use
from cbe3.core.models import User
from cbe3.core.django_assertions import assert_contains


@pytest.fixture
def url():
    return resolve_url('register')


@pytest.fixture
def valid_user():
    return {'username': 'Henrique de Andrade', 'email': 'henrique@email.com'}


@pytest.fixture
def user_same_email():
    return {'username': 'Henrique Conde', 'email': 'henrique@email.com'}


@pytest.fixture
def user_db(db, valid_user):
    return User.objects.create(**valid_user)


def test_register_status_code(client, url, db):
    resp = client.get(url)

    assert resp.status_code == HTTPStatus.OK


def test_register_template(client, url, db):
    resp = client.get(url)

    assert_template_use(resp, 'register_user.html')


def test_register(client: Client, url, valid_user, db):
    resp = client.post(url, data=valid_user)

    user = User.objects.get(pk=1)

    assert user.username == valid_user['username']
    assert user.email == valid_user['email']


def test_email_exists(client, url, user_same_email, user_db):
    resp = client.post(url, data=user_same_email)

    assert User.objects.count() == 1


def test_message_email_already_exist(client, url, user_same_email, user_db):
    resp = client.post(url, data=user_same_email)

    assert_contains(resp, '<p> O email')