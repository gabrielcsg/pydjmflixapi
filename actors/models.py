from django.db import models

NATIONALITIES_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITIES_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name
