
import factory.fuzzy
from factory.django import DjangoModelFactory

from users.models import User


class UserFactory(DjangoModelFactory):
    email = factory.fuzzy.FuzzyText()
    password = factory.PostGenerationMethodCall('set_unusable_password')
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()

    class Meta:
        model = User

    @factory.lazy_attribute_sequence
    def email(self, n):
        return f'{self.first_name}.{self.last_name}_{n}@nowhere.nodomain'.lower()
