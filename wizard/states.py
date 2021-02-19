from wizard.models import Product
from wizard.serializers import MailerBoxSerializer, PolyMailerSerializer


class State:

    @property
    def get_serializer_class(self):
        pass

    def get_price(self):
        pass


class ProductMachine(object):

    def __init__(self):
        self.state = InitState()

    def set_state(self, data):
        self.state = self.state.set_state(data)


class InitState(State):

    def set_state(self, data):
        if data['product_type'] == Product.MAILERBOX:
            return MailerBoxState(data)
        else:
            return PolyMailerState(data)


class MailerBoxState(State):

    def __init__(self, data):
        self.data = data.copy()
        self.get_price()

    @property
    def get_serializer_class(self):
        return MailerBoxSerializer(data=self.data)

    def get_price(self):
        self.data['price'] = (float(self.data['width']) + float(self.data['height']) +
                              float(self.data['length'])) * float(0.1) * float(self.data['quantity'])


class PolyMailerState(State):

    def __init__(self, data):
        self.data = data.copy()
        self.get_price()

    @property
    def get_serializer_class(self):
        return PolyMailerSerializer(data=self.data)

    def get_price(self):
        if self.data['material'] == 'black':
            self.data['price'] = (float(self.data['width']) + float(
                self.data['height'])) * float(0.1) * float(self.data['quantity'])
        else:
            self.data['price'] = (float(self.data['width']) + float(self.data['height'])) * (
                float(0.1) + float(0.15)) * float(self.data['quantity'])
