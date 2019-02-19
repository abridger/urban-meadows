from django.contrib import admin
from .models import (Location,
                     Meadow,
                     Update)


admin.site.register(Location)
admin.site.register(Meadow)
admin.site.register(Update)
