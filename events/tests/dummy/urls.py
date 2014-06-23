from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'dummy/(?P<pk>\d+)/',
        views.DummyView.as_view(),
        name='dummy-detail',
    ),
]
