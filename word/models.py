from django.db import models

class DailyDictionary(models.Model):
    english = models.CharField('English', max_length=128)
    uzbek = models.CharField('Uzbek', max_length=128)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
