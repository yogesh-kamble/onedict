from django.contrib import admin
from .models import EnglishWordDict

# Register your models here.


class EnglishWordDictAdmin(admin.ModelAdmin):
    """Admin for EnglishWordDict
    """
    list_display = ('word',)

admin.site.register(EnglishWordDict, EnglishWordDictAdmin)
