from django.contrib.auth import get_user_model
import factory

from .. import models
from .dummy.models import Dummy


class DummyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Dummy

    name = factory.Sequence('Test {}'.format)


class EventFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Event

    object = factory.SubFactory(DummyFactory)


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()

    username = factory.Sequence('test-user-{}'.format)
    email = factory.Sequence('test-{}@example.com'.format)
