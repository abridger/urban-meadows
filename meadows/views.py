from meadows.filters import LocationFilterBackend
from meadows.models import (Meadow,
                            Update)
from meadows.serializers import (MeadowSerializer,
                                 UpdateSerializer)
from rest_framework import (mixins,
                            permissions,
                            status,
                            viewsets)
from rest_framework.response import Response


class MeadowViewSet(viewsets.ModelViewSet):
    filter_backends = (
        LocationFilterBackend,
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Meadow.objects.all()
    serializer_class = MeadowSerializer

    def create(self, request, *args, **kwargs):
        created_by = request.user.id
        request.data['created_by'] = created_by
        return super(MeadowViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        updated_by = request.user.id
        instance = self.get_object()

        meadow_serializer = MeadowSerializer(
            instance=instance,
            data=request.data
        )
        if meadow_serializer.is_valid():
            meadow_serializer.save()
            update_serializer = UpdateSerializer(
                data={
                    'created_by': updated_by,
                    'meadow': instance.id
                }
            )
            if update_serializer.is_valid():
                update_serializer.save()
                return Response(
                    data=meadow_serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data=update_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                data=meadow_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
