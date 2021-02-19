from rest_framework import serializers

from wizard.models import Offer, Product


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_type',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class MailerBoxSerializer(serializers.ModelSerializer):
    quantity = serializers.FloatField(min_value=200, max_value=1000)
    width = serializers.FloatField(min_value=0, max_value=200)
    height = serializers.FloatField(min_value=0, max_value=200)
    length = serializers.FloatField(min_value=0, max_value=200)

    class Meta:
        model = Product
        fields = ('quantity', 'price', 'width',
                  'height', 'product_type', 'length',)


class PolyMailerSerializer(serializers.ModelSerializer):
    quantity = serializers.FloatField(min_value=200, max_value=1000)
    width = serializers.FloatField(min_value=0, max_value=200)
    height = serializers.FloatField(min_value=0, max_value=200)

    class Meta:
        model = Product
        fields = ('quantity', 'price', 'width',
                  'height', 'product_type', 'material',)


class OfferSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Offer
        fields = '__all__'
