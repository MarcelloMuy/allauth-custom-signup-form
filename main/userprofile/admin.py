'Imported'
from django.contrib import admin
from .models import UserProfile, Profession


class ProfessionAdmin(admin.ModelAdmin):
    """Admin Profession"""
    list_display = (
        'name',
    )


class UserProfileAdmin(admin.ModelAdmin):
    """Admin UserProfile"""
    list_display = (
        'user',
        'profession',
        'experience',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Profession, ProfessionAdmin)
