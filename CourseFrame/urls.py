from django.conf.urls import patterns, include, url
from CourseFrame.views import current_datetime, hours_ahead
from django.contrib import admin
from course import views
from course.models import *
from course.forms import *
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'CourseFrame.views.home', name='home'),
    # url(r'^CourseFrame/', include('CourseFrame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^time/$', current_datetime),
    (r'^admin/', include(admin.site.urls)),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^add_teacher/thanks/$', views.thanks),
    (r'^teacher/add/$', views.add, {'form': TeacherForm}),
    (r'^course/add/$', views.add, {'form': courseForm}),
    (r'^assignment/add/$', views.add, {'form': assignmentForm}),
    (r'^announcement/add/$', views.add, {'form': announcementForm}),
    (r'^resources/add/$', views.add, {'form': resourcesForm}),
    (r'^textbook/add/$', views.add, {'form': textbookForm}),
    (r'^teacher/(?P<id>\d+)/$', views.update, {'form': TeacherForm, 'model': teacher}),
    (r'^course/?P<id>\d+/$', views.update, {'form': courseForm, 'model': course}),
    (r'^assignment/?P<id>\d+/$', views.update, {'form': assignmentForm, 'model': assignment}),
    (r'^announcement/?P<id>\d+/$', views.update, {'form': announcementForm, 'model': announcement}),
    (r'^resources/?P<id>\d+/$', views.update, {'form': resourcesForm, 'model': resources}),
    (r'^textbook/?P<id>\d+/$', views.update, {'form': textbookForm, 'model': textbook}),
)
