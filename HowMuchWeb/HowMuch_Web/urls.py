__author__ = 'Wang'

from django.conf.urls import patterns
from django.conf.urls import url
import HowMuch_Web.views

urlpatterns = patterns('',
                       url(r'^qScore/', HowMuch_Web.views.qScore),
                       url(r'^qCourse/', HowMuch_Web.views.qCourse),
                       url(r'^bind/', HowMuch_Web.views.bind),
                       url(r'^grdms$', HowMuch_Web.views.grdms),
                       )