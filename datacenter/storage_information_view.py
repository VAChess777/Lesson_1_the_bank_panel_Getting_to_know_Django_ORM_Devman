from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visitors_in_storage = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visitors_in_storage:
        delta = get_duration(visit)
        different = format_duartion(delta)
        visitor_serialize = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
             'leaved_at': localtime(visit.leaved_at),
            'duration': str(different).split('.')[0]
        }
        non_closed_visits.append(visitor_serialize)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)


def get_duration(visit):
    start_visit = visit.entered_at
    end_visit = visit.leaved_at
    # local_time = localtime()
    if end_visit:
        delta = end_visit - start_visit
    else:
        delta = localtime() - start_visit
    return delta


def format_duartion(delta):
    seconds = delta.total_seconds()
    hours = abs(int(seconds // 3600))
    minutes = abs(int(seconds % 3600) // 60)
    different = f'{hours}:{minutes}'
    return different