from rest_framework import generics

from .models import Dummy
from .serializers import EventSerializer
from events.views import BaseEventView


class DummyView(generics.RetrieveAPIView):
    model = Dummy


class EventView(BaseEventView):
    serializer_class = EventSerializer
