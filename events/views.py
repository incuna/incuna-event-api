from rest_framework import generics
from rest_framework import permissions


class BaseEventView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user
