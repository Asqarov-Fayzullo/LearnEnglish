from django.urls import path
from .views import DailyDictionaryListAPIView


urlpatterns = [
    path('', DailyDictionaryListAPIView.as_view()),
]