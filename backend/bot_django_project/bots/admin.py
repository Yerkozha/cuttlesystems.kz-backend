from django.contrib import admin

from utils.get_commit_info_from_github_api import get_commit_info_from_github_api
from .models import Bot, Message, Variant, Command

admin.site.site_header = get_commit_info_from_github_api()
admin.site.index_title = 'Bot constructor'


class BotAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'start_message']
    list_filter = ('owner',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'keyboard_type', 'bot']
    list_editable = ['keyboard_type']
    list_filter = ('bot',)


class VariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'current_message', 'next_message', 'display_bot']
    list_filter = ('current_message', 'next_message')


class CommandAdmin(admin.ModelAdmin):
    list_display = ['id', 'bot', 'command', 'description']
    list_editable = ['command', 'description']
    list_filter = ('bot',)


admin.site.register(Bot, BotAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Command, CommandAdmin)
