from django.contrib import admin
from .models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "creater",
        "place_to_do",
        "time_to_do",
        "action_to_do",
        "is_pleasant",
        "related_habit",
        "periodicity",
        "reward",
        "duration",
        "is_public",
    )
    search_fields = ["action_to_do", "time_to_do", "place_to_do"]
    list_filter = ["creater", "is_pleasant", "is_public"]
