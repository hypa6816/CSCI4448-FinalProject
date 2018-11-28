from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from datetime import datetime
from personbook.models import Books
# Create your models here.
class Yearbooks(Books):
    title =  models.CharField(
        max_length=4,
        validators=[
            RegexValidator(
                r'^[0-9]*$',
                'Only characters 0-9 are allowed.'
            ),
            MinLengthValidator(4),
            MaxLengthValidator(4),
        ])
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Yearbooks"






