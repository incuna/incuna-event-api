from rest_framework import status

from .. import models
from . import factories
from .dummy import views
from .utils import APIRequestTestCase


class TestEventView(APIRequestTestCase):
    view_class = views.EventView

    def test_create(self):
        request = self.create_request()
        dummy = factories.DummyFactory.create()
        data = {'object': dummy.get_absolute_url(request)}

        request = self.create_request('post', data=data)
        view = self.view_class.as_view()
        response = view(request)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg=response.data,
        )

        event = models.Event.objects.get()
        self.assertEqual(event.object, dummy)
        self.assertEqual(event.user, request.user)
