from django.contrib import admin
from .models import DailyDictionary

class DailyDictionaryAdmin(admin.ModelAdmin):
    list_display = ['english', 'uzbek', 'views', 'created_at']


admin.site.register(DailyDictionary, DailyDictionaryAdmin)