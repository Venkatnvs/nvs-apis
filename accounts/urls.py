from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='accounts-login' ),
    path('register/', Registration.as_view(), name='accounts-register' ),
    path('', Registration.as_view(), name='accounts-register-blank' ),
    path('logout/', Logout.as_view(), name='accounts-logout' ),
    path('forget-password/', ForgetPassword.as_view(), name='accounts-forget-password' ),
    path('activate-user/<uidb64>/<token>', Verification.as_view(), name='accounts-activate'),
    path('reset-user-password/<uidb64>/<token>', SetNewPassword.as_view(), name='accounts-reset-user-password'),

    path('complete-account/', CompleteSocialAccount.as_view(), name='accounts-complete-social' ),
]