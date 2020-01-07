from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='favicon.ico')),
    path('', views.index, name='index'),
]
