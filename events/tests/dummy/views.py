from rest_framework import generics

from .models import Dummy


class DummyView(generics.RetrieveAPIView):
    model = Dummy
