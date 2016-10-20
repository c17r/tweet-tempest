from django.conf.urls import url, include

from backend import views

urlpatterns = [
    url(r'^$', views.HomepageView.as_view()),
    url('api/twitter/info/$', views.TwitterInfoView.as_view()),
    url('api/twitter/tweet/$', views.SendTweetView.as_view()),
]
