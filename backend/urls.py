from django.urls import path

from backend import views

urlpatterns = [
    path('', views.HomepageView.as_view()),
    path('api/twitter/info/', views.TwitterInfoView.as_view()),
    path('api/twitter/tweet/', views.SendTweetView.as_view()),
]
