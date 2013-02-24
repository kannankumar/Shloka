from django.conf.urls.defaults import *
from quizzy_video.views import quizzy_video
from pro_scheduler.views import set_scheduling_question

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^quizzy_video/(\d{1,2})/$','quizzy_video.views.quizzy_video'),
    (r'^interactive_process_scheduling/(\d{1,2})/$','pro_scheduler.views.set_scheduling_question'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
        # Serve static files in debug.
        urlpatterns += patterns('',
#                (r'^quizzy_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,'show_indexes' : True}),
              (r'^shloka_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes' : True}),

	)

