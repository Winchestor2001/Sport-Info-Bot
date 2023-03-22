from django.contrib import admin
from .models import *


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'language', 'team']


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']


@admin.register(LigaTable)
class LigaTableAdmin(admin.ModelAdmin):
    list_display = ['liga', 'team', 'score']
    list_filter = ['liga']


@admin.register(LigaPlayer)
class LigaPlayerAdmin(admin.ModelAdmin):
    list_display = ['liga', 'team', 'player']
    list_filter = ['liga']


@admin.register(TopTeam)
class TopTeamAdmin(admin.ModelAdmin):
    list_display = ['team', 'rate']


@admin.register(GameCalendar)
class GameCalendarAdmin(admin.ModelAdmin):
    list_display = ['liga', 'tour', 'team', 'date']
    list_filter = ['liga']
