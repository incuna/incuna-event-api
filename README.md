# incuna-event-api

## Installation

Install the package

    pip install incuna-event-api

Add to installed apps:

    INSTALLED_APPS = (
        'events',
    )

## Event Model

The `Event` model defines `object`, `time` and `user` fields.

## Event Serializer

You will need a custom `EventSerializer` to specify the related `object`s an `Event` can refer to:

    from generic_relations.relations import GenericRelatedField
    from rest_framework.serializers import HyperlinkedRelatedField

    class EventSerializer(serializers.ModelSerializer):
        object = GenericRelatedField(
            {
                Model: HyperlinkedRelatedField(view_name='model-detail'),
            },
            read_only=False,
        )

        class Meta:
            fields = ['object']
            model = Event

## Event View

You can extend the `BaseEventView` adding your `EventSerializer`. The `BaseEventView` accepts a post request with the url of the related object:

    {
        'object': 'http://example.com/model/17'
    }

An `Event` is created with `user` set to the authenticated user and `object` set to the related object.
