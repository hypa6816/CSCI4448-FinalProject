from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime
# Create your models here.
class Personbooks(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Personbooks"




