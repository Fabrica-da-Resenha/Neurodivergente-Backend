from django.contrib import admin
from core.Neurodivergente.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = ("id", "user", "name", "gender",)
    