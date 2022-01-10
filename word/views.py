from rest_framework.generics import ListAPIView

from .models import DailyDictionary
from .serializers import DailyDictionarySerializer


class DailyDictionaryListAPIView(ListAPIView):
    queryset = DailyDictionary.objects.all()
    serializer_class = DailyDictionarySerializer