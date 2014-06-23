from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from ...models import Event
from .models import Dummy


class EventSerializer(serializers.ModelSerializer):
    object = GenericRelatedField(
        {Dummy: serializers.HyperlinkedRelatedField(view_name='dummy-detail')},
        read_only=False,
    )

    class Meta:
        fields = ['object']
        model = Event
