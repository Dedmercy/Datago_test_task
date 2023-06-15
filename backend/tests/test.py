import pytest
from fastapi.testclient import TestClient
from fastapi import status
from fastapi.encoders import jsonable_encoder

from backend.app.app import app
from backend.app.schemas.user import UserCreateSchema
from backend.app.schemas.transaction import TransactionCreateSchema

tested_user = UserCreateSchema(
    username='testuser',
    password='testpass',
    first_name='tested',
    middle_name='tested',
    last_name='tested',
    email='test@ex.com',
    phone='blabla'
)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def test_user():
    return {"username": "testuser", "password": "testpass"}


def test_registration(client):
    """
        Creating a new user test, successfully when we enter a new user, else get error
    """

    response = client.post('/auth/registration', json=jsonable_encoder(tested_user))

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['username'] == 'testuser'


def test_login(client, test_user):
    """
        Testing login endpoint
    """
    response = client.post('/auth/login', data=test_user)

    assert response.status_code == status.HTTP_200_OK
    token = response.json()["access_token"]
    assert token is not None
    return token


def test_get_current_account(client, test_user):
    """
        Testing curren user info
    """
    token = test_login(client, test_user)
    response = client.get('/account/me', headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == "testuser"


def test_add_transaction(client, test_user):
    """
        Testing add new transaction
    """
    token = test_login(client, test_user)
    response = client.post(
        '/tracking/add',
        headers={"Authorization": f"Bearer {token}"},
        json=jsonable_encoder(
            TransactionCreateSchema(
                category='beauty',
                money=1000
            )
        )
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['money'] == str(1000)


def test_get_all_transactions(client, test_user):
    """
        Testing get all transaction for current user
    """
    token = test_login(client, test_user)
    response = client.get(
        '/tracking/all',
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK


def test_get_transaction_by_category(client, test_user):
    """
        Testing get all transaction with category for current user
    """
    token = test_login(client, test_user)
    response = client.post(
        '/tracking/category',
        headers={"Authorization": f"Bearer {token}"},
        params=jsonable_encoder({'category': 'beauty'})
    )

    assert response.status_code == status.HTTP_200_OK
