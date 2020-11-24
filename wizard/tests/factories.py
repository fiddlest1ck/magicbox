import factory.fuzzy
from factory.django import DjangoModelFactory

from wizard.models import Offer, Product


class OfferFactory(DjangoModelFactory):
    class Meta:
        model = Offer

    state = factory.fuzzy.FuzzyChoice(Offer.STATE_CHOICES)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    quantity = 300.0
    price = 0.0
    width = 200.0
    height = 200.0
    length = 200.0
    material = factory.fuzzy.FuzzyChoice(Product.MATERIAL_TYPES)
    product_type = factory.fuzzy.FuzzyChoice(Product.PRODUCT_TYPES)
