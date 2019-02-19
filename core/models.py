from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    def _generate_username(self, first_name, last_name):
        import random
        import string
        suffix = ''.join(
            random.choice(string.digits) for _ in range(6)
        )
        username = ''.join([
            first_name.lower().replace(' ', ''),
            last_name.lower().replace(' ', ''),
            suffix
        ])
        try:
            User.objects.get(username=username)
            return self.generate_username(
                first_name,
                last_name
            )
        except User.DoesNotExist:
            return username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self._generate_username(
                self.first_name,
                self.last_name
            )
        super().save(
            *args,
            **kwargs
        )
