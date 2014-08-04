# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from poll.models import Poll, Vote, Item
from poll import views
register = template.Library()

@register.simple_tag(takes_context=True)
def poll(context):
    request = context['request']

    try:
        poll = Poll.published.latest("date")
    except ObjectDoesNotExist:
        return ''
    
    if poll.get_cookie_name() not in request.COOKIES\
            and not Vote.objects.filter(ip=request.META['REMOTE_ADDR'], poll=poll)\
                    .count():
        return views.poll(context['request'], poll.id).content
    else:
        return views.result(context['request'], poll.id).content
    
@register.simple_tag                                                                                                                         
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100

@register.filter
def poll_items(poll_pk):
    return Item.objects.filter(poll__pk=poll_pk)