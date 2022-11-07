from datetime import timedelta

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .storage_information_view import format_duartion
from .storage_information_view import get_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in passcard_visits:
        delta = get_duration(visit)
        different = format_duartion(delta)
        flag = is_visit_long(delta)
        visit_serialize = {
            'entered_at': visit.entered_at,
            'duration': different,
            'is_strange': flag
        }
        this_passcard_visits.append(visit_serialize)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def is_visit_long(delta):
    result = delta > timedelta(minutes=60)
    return result