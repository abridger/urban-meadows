from django.contrib.gis.geos import fromstr
from rest_framework import filters


class LocationFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        """
        Check the query params for a location query. If present,
        filter the queryset based on the values provided, with an
        optional radius given in metres. Otherwise, just return
        the queryset.
        """
        location_query = request.query_params.get(
            'location',
            None
        )
        # Default radius of 2km
        radius_query = request.query_params.get(
            'radius',
            2000
        )
        if location_query:
            lat, lng = location_query.split(',')
            reference_location = fromstr(
                'POINT(%s %s)' % (
                    lat,
                    lng
                )
            )
            return queryset.filter(
                location__coordinates__distance_lte=(
                    reference_location,
                    radius_query
                )
            )
        return queryset
