from django.contrib import admin
from .models import DailyDictionary, TypeOfWord

class DailyDictionaryAdmin(admin.ModelAdmin):
    list_display = ['english', 'uzbek', 'views', 'created_at']


class TypeOfWordAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


admin.site.register(DailyDictionary, DailyDictionaryAdmin)
admin.site.register(TypeOfWord, TypeOfWordAdmin)
