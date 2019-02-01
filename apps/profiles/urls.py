from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from profiles.forms import SignInForm
from profiles.views import SingUpFormView

urlpatterns = [
    path(
        'sign-up/',
        SingUpFormView.as_view(),
        name='sign_up_form_view'
    ),

    path(
        'sign-in/',
        LoginView.as_view(
            form_class=SignInForm
        ),
        name='log_in_django_view'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout_view'
    )
]
