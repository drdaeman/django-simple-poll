# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from poll.models import *
from poll import views
register = template.Library()

@register.simple_tag(takes_context=True)
def poll(context):
    request = context['request']

    try:
        poll = Poll.published.latest("date")
    except:
        return ''
    
    if not poll.vote_set.filter(user=request.user):
        return views.poll(context['request'], poll.id).content
    else:
        return views.result(context['request'], poll.id).content
    
@register.simple_tag                                                                                                                         
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100
