from django.test import TestCase

from .. import models


class TestEvent(TestCase):
    def test_fields(self):
        expected_fields = {
            'id',
            'user',
            'time',
            'content_type',
            'object_id',
        }
        fields = models.Event._meta.get_all_field_names()
        self.assertCountEqual(fields, expected_fields)