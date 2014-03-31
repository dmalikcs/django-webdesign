from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'webdesign.views.home', name='webdesign_home'),

                       )
