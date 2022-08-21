from django.urls import path

from courses.views import WelcomeView

urlpatterns = [
    path('', WelcomeView.as_view()),
]
