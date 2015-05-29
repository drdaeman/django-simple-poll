from __future__ import absolute_import

from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import Poll, Item
from .. import views

register = template.Library()


@register.simple_tag(name="poll", takes_context=True)
def poll_tag(context, poll_id=None, user=False):
    request = context["request"]

    try:
        poll = Poll.published
        if user is not False:
            poll = poll.filter(user=user)
        if poll_id is not None:
            poll = poll.get(id=poll_id)
        else:
            poll = poll.latest("publication_date")
    except ObjectDoesNotExist:
        return ""

    if request.user.is_authenticated():
        if poll.vote_set.filter(user=request.user):
            return views.result(context["request"], poll.id).content
    return views.poll(context["request"], poll.id).content


@register.simple_tag
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100


@register.filter
def poll_items(poll_pk):
    return Item.objects.filter(poll__pk=poll_pk)
