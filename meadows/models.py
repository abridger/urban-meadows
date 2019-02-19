from django.conf import settings
from django.contrib.gis.db import models
import uuid


# Create your models here.
class Location(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    address_1 = models.CharField(
        blank=True,
        max_length=100,
        null=True
    )
    address_2 = models.CharField(
        blank=True,
        max_length=100,
        null=True
    )
    city = models.CharField(
        blank=True,
        max_length=50,
        null=True
    )
    coordinates = models.PointField()
    meadow = models.OneToOneField(
        'meadows.Meadow',
        on_delete=models.CASCADE
    )

    def __str(self):
        if self.meadow:
            return '%s location' % self.meadow
        return 'Unassigned location'


class Meadow(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='meadows_created'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Update(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        on_delete=models.CASCADE,
        null=True,
        related_name='meadows_updated'
    )
    meadow = models.ForeignKey(
        'meadows.Meadow',
        on_delete=models.CASCADE
    )

    def __str(self):
        if self.meadow:
            return '%s location' % self.meadow
        return 'Unassigned update'
