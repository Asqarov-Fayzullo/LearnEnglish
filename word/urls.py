from django.urls import path
from .views import DailyDictionaryListAPIView, TypeOfWordListAPIView


urlpatterns = [
    path('', DailyDictionaryListAPIView.as_view()),
    path('type/', TypeOfWordListAPIView.as_view()),
]