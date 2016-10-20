from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'logout/$', logout_then_login, name='logout'),

    url(r'', include('backend.urls')),
]
