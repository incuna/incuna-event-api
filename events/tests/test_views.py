from rest_framework import status

from .. import models
from . import factories
from .dummy import views
from .utils import APIRequestTestCase


class TestEventView(APIRequestTestCase):
    view_class = views.EventView

    def setUp(self):
        request = self.create_request()
        self.dummy = factories.DummyFactory.create()
        self.data = {'object': self.dummy.get_absolute_url(request)}

    def test_create(self):
        request = self.create_request('post', data=self.data)
        view = self.view_class.as_view()
        response = view(request)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg=response.data,
        )

        event = models.Event.objects.get()
        self.assertEqual(event.object, self.dummy)
        self.assertEqual(event.user, request.user)

    def test_create_anonymous_user(self):
        request = self.create_request('post', auth=False, data=self.data)
        view = self.view_class.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
