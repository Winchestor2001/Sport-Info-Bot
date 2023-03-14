from django.contrib import admin
from .models import *


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']


@admin.register(BotContext)
class BotContextAdmin(admin.ModelAdmin):
    pass


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ['name']


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







