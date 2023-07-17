from django.db import models


class AnimalImage(models.Model):
    CHOICES_SP = [('cat', 'Cat'), ('dog', 'Dog')]
    CHOICES_TP = [('png', 'png'), ('gif', 'gif'), ('jpeg', 'jpeg')]
    url = models.URLField()
    speicies = models.CharField(
        default='cat',
        max_length=5,
        choices=CHOICES_SP
    )
    create_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        default='png',
        max_length=5,
        choices=CHOICES_TP
    )
