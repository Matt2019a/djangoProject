from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^$', views.activities),
    url(r'^search', views.getActivities)
]
