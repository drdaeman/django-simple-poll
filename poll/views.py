from __future__ import absolute_import
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .utils import set_cookie
from .models import Item, Poll, Vote


def vote(request, poll_pk):
    if request.is_ajax():
        try:
            poll = Poll.objects.get(pk=poll_pk)
        except Poll.DoesNotExist:
            return HttpResponse("Wrong parameters", status=400)

        item_pk = request.GET.get("item", False)
        if not item_pk:
            return HttpResponse("Wrong parameters", status=400)

        try:
            item = Item.objects.get(pk=item_pk)
        except Item.DoesNotExist:
            return HttpResponse("Wrong parameters", status=400)

        if request.user.is_authenticated():
            user = request.user
        else:
            user = None

        Vote.objects.get_or_create(
            poll=poll,
            user=user,
            defaults=dict(
                ip=request.META["REMOTE_ADDR"],
                item=item,
            )
        )

        response = HttpResponse(status=200)
        set_cookie(response, poll.get_cookie_name(), poll_pk)

        return response
    return HttpResponse(status=400)


def poll(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except Poll.DoesNotExist:
        return HttpResponse("Wrong parameters", status=400)

    items = Item.objects.filter(poll=poll)

    return render_to_response("poll/poll.html", {
        "poll": poll,
        "items": items,
    }, context_instance=RequestContext(request))


def result(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except Poll.DoesNotExist:
        return HttpResponse("Wrong parameters", status=400)

    items = Item.objects.filter(poll=poll)
    bare = request.GET.get("bare", None) is not None
    template_name = "poll/result_bare.html" if bare else "poll/result.html"

    return render_to_response(template_name, {
        "poll": poll,
        "items": items,
    }, context_instance=RequestContext(request))


def all_results(request):
    polls = Poll.objects.filter(status=1)
    return render_to_response("poll/all_results.html", {
        "polls": polls,
    }, context_instance=RequestContext(request))
