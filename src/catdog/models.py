from django.db import models


class Animals(models.Model):
    url = models.URLField()
    speicies = models.CharField(
        default='cat',
        max_length=5,
        choices=[('cat', 'Cat'), ('dog', 'Dog')]
    )
    create_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        default='png',
        max_length=5,
        choices=[('png', 'png'), ('gif', 'gif'), ('jpeg', 'jpeg')]
    )
