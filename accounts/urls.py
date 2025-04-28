from django.urls import path
from accounts.views.signin import Signin


urlpatterns = [
    path('signin/', Signin.as_view()),
]