from django.urls import path, re_path
from . import views


urlpatterns = [

]

urlpatterns += [
    re_path(r'^accounts/login/$', views.login_view, name='login'),
    re_path(r'^accounts/signup/$', views.UserSignUp.as_view(), name='register'),

    re_path(r'^accounts/logout/$', views.logout_view, name='logout'),
    # path(r'^accounts/password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
    # path(r'^accounts/password_change/done/$', views.PasswordChangeDoneView.as_view(),
    # name='password_change_done'),
    # path(r'^accounts/password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    # path(r'^accounts/password_reset/done/$', views.PasswordResetDoneView.as_view(),
    # name='password_reset_done'),
    # path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path(r'^accounts/reset/done/$', views.PasswordResetCompleteView.as_view(),
    # name='password_reset_complete'),
]

