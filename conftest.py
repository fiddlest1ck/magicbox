import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.tests.factories import UserFactory


@pytest.fixture(scope='session')
def user_data():
    return dict(
        email='john.doe@nowhere.nodomain', first_name='John', last_name='Doe', is_active=True)


@pytest.fixture
def user_client(user_data):
    user_data['user_type'] = User.CLIENT
    return UserFactory(**user_data)


@pytest.fixture
def superuser(user_data):
    user_data['user_type'] = User.SUPERUSER
    return UserFactory(**user_data)


@pytest.fixture
def user_salesman(user_data):
    user_data['user_type'] = User.SALESMAN
    return UserFactory(**user_data)


@pytest.fixture
def client_client(client, user_client):
    refresh = RefreshToken.for_user(user_client)
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION='Bearer {}'.format(refresh.access_token))
    client.user = user_client
    return client


@pytest.fixture
def superuser_client(client, superuser):
    refresh = RefreshToken.for_user(superuser)
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION='Bearer {}'.format(refresh.access_token))
    client.user = superuser
    return client


@pytest.fixture
def salesman_client(client, user_salesman):
    refresh = RefreshToken.for_user(user_salesman)
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION='Bearer {}'.format(refresh.access_token))
    client.user = user_salesman
    return client


@pytest.fixture
def unauthorized_client():
    return APIClient()
