from rest_framework import serializers
from .models import DailyDictionary

class DailyDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyDictionary
        fields = ('id','english','uzbek')