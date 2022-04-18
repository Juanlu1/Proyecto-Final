
from django.urls import path
from .views import iniciar_sesion, inicio, registrar, editar_user, about_me
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="inicio"),

    path("accounts/login/", iniciar_sesion, name ="login"),
    path("accounts/logout/", LogoutView.as_view(template_name="log2/logout.html"), name="logout"),
    path("accounts/signup/", registrar, name="registrar"),
    path("accounts/profile/", editar_user, name="editar_user"),

    path("about/", about_me, name="about"),
]
