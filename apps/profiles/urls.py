from django.urls import path
from django.contrib.auth.views import LoginView

from profiles.views import SingUpFormView

urlpatterns = [
    path(
        'sign-up/',
        SingUpFormView.as_view(),
        name='sign_up_form_view'
    ),

    path(
        'sign-in/',
        LoginView.as_view(),
        name='log_in_django_view'
    )
]
