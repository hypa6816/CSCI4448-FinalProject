from django.db import models
from datetime import datetime

# Factory Method for Presents
def makePresent(type):
    types = {
        'Sentimental': SentimentalPresent(), 
        'Purchased': PurchasedPresent(),
        'Crafted': CraftedPresent()
    }
    return types[type]

# Class to Query Depending on Type
class PresentQuerySet(models.QuerySet):
    def sentimentalPresents(self):
        return self.filter(type='Sentimental')

    def purchasedPresents(self):
        return self.filter(type='Purchased')

    def craftedPresents(self):
        return self.filter(type='Crafted')

# Manager for Presents Model
class PresentsManager(models.Manager):
    def makePresent(self, type_input):
        present = self.create(makePresent(type_input))
        return present
    def get_queryset(self):
        return PresentQuerySet(self.model, using=self._db)

    def momento(self):
        return self.momento

    def given_to(self):
        return self.given_to

# Presents Model
class Presents(models.Model):
    title = models.CharField(max_length = 200)
    memento = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    given_at = models.DateTimeField(default=datetime.now)
    given_to = models.CharField(max_length = 200)
    type_input = models.CharField(max_length=200, default="Purchased")

    objects = PresentsManager()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Presents"

# Different Present Objects that can be created
class SentimentalPresent(object):
    title = models.CharField(max_length = 200)
    color = 'green'
class PurchasedPresent(object):
    title = models.CharField(max_length = 200)
    color = 'blue'
class CraftedPresent(object):
    color = 'yellow'
    title = models.CharField(max_length = 200)

