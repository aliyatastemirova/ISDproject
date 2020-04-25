from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", user_views.HomeView.as_view(), name="home"),
    path("register/", user_views.RegistrationFormView.as_view(), name="register"),
    path("profile/", user_views.AccountView.as_view(), name="account"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
