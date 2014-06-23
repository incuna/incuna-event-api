from rest_framework import generics


class BaseEventView(generics.CreateAPIView):
    def pre_save(self, obj):
        obj.user = self.request.user
