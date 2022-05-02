from django.shortcuts import resolve_url

from cbe3.core.models import User


def test_delete_user(client, users):
    users = users[0]

    client.get(resolve_url('delete_user', id=users.id))

    assert User.objects.count() == 1
