from django.db import models
from django.contrib.auth.models import User


class Crypto(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.CharField(max_length=15)
    total_supply = models.BigIntegerField( null=True )
    price = models.PositiveBigIntegerField( null=True )
    market_cap = models.PositiveBigIntegerField(null=True)
    volume_change_24h = models.FloatField( null=True)
    percent_change_24h = models.FloatField(null=True)
    user_favourite = models.ManyToManyField(
        User, related_name='favourite')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crypto_currencies'
        ordering = ['-name', 'price']
        indexes = [
            models.Index(fields=['name', 'slug'])
        ]
