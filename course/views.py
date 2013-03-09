from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from course.models import teacher
from course.forms import ContactForm


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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})
