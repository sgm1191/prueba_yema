from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^agendar', views.citas.as_view(), name='citas_post'),
]