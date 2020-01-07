from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    #url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico'), name='favicon'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    path('', views.index, name='index'),
]
