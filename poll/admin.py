from django.contrib import admin
from poll.models import *
from django.utils.translation import gettext as _

class PollItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'vote_count', 'is_published')
    inlines = [PollItemInline,]

admin.site.register(Poll, PollAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('item', 'poll', 'user', 'first_name', 'last_name', 'ip', 'datetime')
    list_filter = ('poll', 'datetime')
    search_fields = ['poll__title', 'item__value', 'user__first_name', 'user__last_name', 'user__email']

admin.site.register(Vote, VoteAdmin)
