from rest_framework.generics import ListAPIView

from .models import DailyDictionary, TypeOfWord
from .serializers import DailyDictionarySerializer, TypeOfWordSerializer


class DailyDictionaryListAPIView(ListAPIView):
    queryset = DailyDictionary.objects.all()
    serializer_class = DailyDictionarySerializer

class TypeOfWordListAPIView(ListAPIView):
    queryset = TypeOfWord.objects.all()
    serializer_class = TypeOfWordSerializer