from . import factories
from .dummy import serializers
from .utils import APIRequestTestCase


class TestEventSerializer(APIRequestTestCase):
    def test_deserialize(self):
        request = self.create_request('post')
        context = {'request': request}

        dummy = factories.DummyFactory.create()

        data = {
            'object': dummy.get_absolute_url(request),
        }

        serializer = serializers.EventSerializer(data=data, context=context)
        self.assertTrue(serializer.is_valid())
