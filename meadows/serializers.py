from rest_framework import serializers
from meadows.models import (Location,
                            Meadow,
                            Update)


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        request = self.context.get('request', None)
        if request:
            fields = request.query_params.get('fields', None)
            if fields:
                fields = fields.split(',')
                # Drop any fields that are not specified
                # in the `fields` argument.
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)


class LocationSerializer(DynamicFieldsModelSerializer):
    coordinates = serializers.SerializerMethodField()

    def get_coordinates(self, location):
        return {
            'lat': location.coordinates.x,
            'lng': location.coordinates.y
        }

    class Meta:
        model = Location
        fields = (
            'id',
            'address_1',
            'address_2',
            'city',
            'coordinates'
        )


class UpdateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Update
        fields = (
            'id',
            'created_at',
            'created_by',
            'meadow',
        )


class MeadowSerializer(DynamicFieldsModelSerializer):
    location = LocationSerializer(
        allow_null=True,
        required=False
    )
    updates = UpdateSerializer(
        allow_null=True,
        required=False,
        many=True,
        source="update_set"
    )

    class Meta:
        model = Meadow
        fields = (
            'id',
            'created_at',
            'created_by',
            'description',
            'location',
            'name',
            'updates',
        )
