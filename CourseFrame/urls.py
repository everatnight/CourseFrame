from django.conf.urls import patterns, include, url
from CourseFrame.views import current_datetime, hours_ahead
from django.contrib import admin
from course import views
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
    (r'^contact/thanks/$', views.thanks),
    (r'^contact/$', views.contact),
)
