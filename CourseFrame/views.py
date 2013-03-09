from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    # try:
    #     #offset = int(offset)
    # except ValueError:
    #     raise Http404()
    return
