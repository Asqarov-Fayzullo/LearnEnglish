from django.db import models


class TypeOfWord(models.Model):
    title = models.CharField('English', max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Type of Word'

    def __str__(self):
        return self.title

class DailyDictionary(models.Model):
    type = models.ForeignKey(TypeOfWord, on_delete=models.CASCADE, related_name='type')
    english = models.CharField('English', max_length=128)
    uzbek = models.CharField('Uzbek', max_length=128)
    views = models.IntegerField(default=0)
    right = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
