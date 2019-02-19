from django.contrib.gis.geoip2 import (GeoIP2,
                                       GeoIP2Exception)
from django.http import HttpResponse
from geoip2.errors import AddressNotFoundError

geolocator = GeoIP2()


def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print('x_forwarded_for', x_forwarded_for)
    print('REMOTE_ADDR', request.META.get('REMOTE_ADDR'))
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def _get_client_lat_lon(client_ip):
    return geolocator.lat_lon(client_ip)


def index(request):
    client_ip = _get_client_ip(request)
    try:
        lat, lon = _get_client_lat_lon(client_ip)
        return HttpResponse(
            'Hi there! It looks like you\'re latitude is %s, and your longitude is %s' % (
                lat,
                lon
            )
        )
    except AddressNotFoundError:
        return HttpResponse(
            'Hi there! It looks like we couldn\'t find your location.'
        )
