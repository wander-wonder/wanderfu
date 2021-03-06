from django.urls import path
from pip._vendor.distro import name

from . import views
#用内置方法实现登录和退出
from django.contrib.auth import views as auth_views

app_name= "account"

urlpatterns = [
    #path('login/', views.user_login, name='user_login'),
    path('showxiaoxin/',views.showxiaoxin,name='showxiaoxin'),
    path('add/',views.add,name='add'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name="account/password_change_form.html", success_url="/account/password-change-done/"),
         name='password_change'),

    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"),
         name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name="account/password_reset_form.html",
        email_template_name="account/password_reset_email.html",
        success_url='/acount/password-reset-done/'),
         name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="account/password_reset_confirm.html",
             success_url='/account/password-reset-complet/'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]