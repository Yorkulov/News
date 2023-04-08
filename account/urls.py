from django.urls import path
from .views import userLogin, dashboard, SignUpView , user_register, edit_user, EditUserView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView

urlpatterns = [
    # path('login/', userLogin, name="LoginForm"),
    path('login/', LoginView.as_view(), name="LoginView"),
    path('logout/', LogoutView.as_view(), name="LogoutView"),
    path('profile/', dashboard, name="UserProfile"),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', user_register, name="user_register"),
    # path('signup/', SignUpView.as_view(), name="user_register"),
    # path('profile/edit', edit_user, name="edit_user_form"),
    path('profile/edit', EditUserView.as_view(), name='edit_user'),
]
