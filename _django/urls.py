from django.urls import path, include
from django.contrib.auth.views import logout_then_login

urlpatterns = (
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_then_login, name='logout'),

    path('', include('backend.urls')),
)
