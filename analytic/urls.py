from django.urls import path

from .views import AnalyticView, UserView

urlpatterns = [
    path("analitic/likes/", AnalyticView.as_view()),
    path("analitic/users/", UserView.as_view()),
]
