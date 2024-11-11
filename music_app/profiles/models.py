from django.core.validators import MinLengthValidator
from django.db import models

from music_app.profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator()
        ],
     )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)