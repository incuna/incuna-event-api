from django.conf.urls import include, url


urlpatterns = [
    url('', include('events.tests.dummy.urls')),
]
