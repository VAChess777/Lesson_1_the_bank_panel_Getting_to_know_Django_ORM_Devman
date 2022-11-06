from datetime import timedelta

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .storage_information_view import format_duartion
from .storage_information_view import get_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in passcard_visits:
        delta = get_duration(visit)
        flag = is_visit_long(visit, delta, compare_minutes=timedelta(minutes=60))
        visit_serialize = {
            'entered_at': visit.entered_at,
            'duration': str(format_duartion(delta)).split('.')[0],
            'is_strange': flag
        }
        this_passcard_visits.append(visit_serialize)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def is_visit_long(visit, delta, compare_minutes=timedelta(minutes=60)):
    if delta > compare_minutes:
        return True
    else:
        return False