from django.db import models
from rest_framework.reverse import reverse


class Dummy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self, request=None):
        return reverse('dummy-detail', kwargs={'pk': self.pk}, request=request)
