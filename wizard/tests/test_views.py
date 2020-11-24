import pytest
from django.urls import reverse

from wizard.tests.factories import OfferFactory


@pytest.mark.django_db
def test_list_offers(superuser_client):
    OfferFactory.create()
    response = superuser_client.get(reverse('offer-list'))
    assert response.data['count'] == 1


@pytest.mark.django_db
def test_client_list_offers(client_client):
    OfferFactory.create()
    response = client_client.get(reverse('offer-list'))
    assert response.data['detail'] == 'You do not have permission to perform this action.'


@pytest.mark.django_db
def test_create_product_from_offer(superuser_client):
    offer = OfferFactory.create(state='created')
    product_data = {"quantity": 200,
                    "product_type": "mailerbox",
                    "width": 200,
                    "height": 200,
                    "length": 100
                    }
    response = superuser_client.post(
        reverse('offer-product-create', kwargs={'pk': offer.pk}), data=product_data)
    assert response.data['quantity'] == 200.0
    response = superuser_client.get(reverse('offer-list'))
    assert response.data['count'] == 1
    assert response.data['results'][0]['products'][0]['quantity'] == 200.0


@pytest.mark.django_db
def test_create_product_rejected_offer(superuser_client):
    offer = OfferFactory.create(state='rejected')
    product_data = {"quantity": 200,
                    "product_type": "mailerbox",
                    "width": 200,
                    "height": 200,
                    "length": 100
                    }
    response = superuser_client.post(
        reverse('offer-product-create', kwargs={'pk': offer.pk}), data=product_data)
    assert response.data == 'Nie można dodawać produktów do oferty w statusie rejected'


@pytest.mark.django_db
def test_reject_offer(client_client):
    offer = OfferFactory.create(state='created')
    response = client_client.post(
        reverse('offer-reject', kwargs={'pk': offer.pk}))
    assert response.data == 'Ofertę odrzucono'


@pytest.mark.django_db
def test_accept_offer(client_client):
    offer = OfferFactory.create(state='created')
    response = client_client.post(
        reverse('offer-accept', kwargs={'pk': offer.pk}))
    assert response.data == 'Zaakceptowano ofertę'


@pytest.mark.django_db
def test_wrong_product_type(superuser_client):
    offer = OfferFactory.create(state='created')
    product_data = {"quantity": 200,
                    "product_type": "asd",
                    "width": 200,
                    "height": 200,
                    "length": 100}
    response = superuser_client.post(
        reverse('offer-product-create', kwargs={'pk': offer.pk}), data=product_data)
    assert str(response.data['product_type'][0]
               ) == '"asd" is not a valid choice.'


@pytest.mark.django_db
def test_price(superuser_client):
    offer = OfferFactory.create(state='created')
    product_data = {"quantity": 200,
                    "product_type": "mailerbox",
                    "width": 200,
                    "height": 200,
                    "length": 100}
    response = superuser_client.post(reverse('offer-product-create',
                                             kwargs={'pk': offer.pk}), data=product_data)
    assert response.data['price'] == 10000.0
    product_data = {"quantity": 200,
                    "product_type": "polymailer",
                    "width": 200,
                    "height": 200,
                    "material": "black"}
    response = superuser_client.post(reverse('offer-product-create',
                                             kwargs={'pk': offer.pk}), data=product_data)
    assert response.data['price'] == 8000.0
    product_data = {"quantity": 200,
                    "product_type": "polymailer",
                    "width": 200,
                    "height": 200,
                    "material": "transparent"}
    response = superuser_client.post(reverse('offer-product-create',
                                             kwargs={'pk': offer.pk}), data=product_data)
    assert response.data['price'] == 20000.0
