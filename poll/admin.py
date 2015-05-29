from __future__ import absolute_import
from django.contrib import admin
from .models import *


class PollItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15
    readonly_fields = ["vote_count"]


class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date", "status", "vote_count")
    inlines = [PollItemInline, ]


admin.site.register(Poll, PollAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("item", "poll", "user", "first_name", "last_name", "ip", "datetime")
    list_filter = ("poll", "datetime")
    search_fields = ["poll__title", "item__value", "user__first_name", "user__last_name", "user__email"]


admin.site.register(Vote, VoteAdmin)
