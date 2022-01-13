from rest_framework import serializers
from .models import DailyDictionary, TypeOfWord

class DailyDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyDictionary
        fields = ('id','type','english','uzbek', 'views', 'right', 'wrong', 'created_at')

class TypeOfWordSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeOfWord
        fields = ('id','title','created_at')