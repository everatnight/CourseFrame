from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from course.models import teacher, course, assignment, announcement, resources, textbook
from course.forms import TeacherForm


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        teachers = teacher.objects.filter(title__icontains=q)
        return render_to_response('search_result.html',
                                  {'teachers': teachers, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})


def thanks(request):
    return render_to_response('Thanks.html')


def add(request, form):
    #todo: auth
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_obj/')
    else:
        form = TeacherForm()
    return render_to_response('contact_form.html', {'form': form})


def update(request, eid, form, model):
    #todo auth
    print eid
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_obj/')
    else:
        form = form(instance=model.objects.filter(id=eid))
    return render_to_response('contact_form.html', {'form': form})
