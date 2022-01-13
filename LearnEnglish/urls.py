from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include


def HomeView(request):
    return HttpResponse("Saytimizning front-end qismi tayyorlanmoqda, Bizning adress @IELTS2022bot.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('api/', include('word.urls')),
]