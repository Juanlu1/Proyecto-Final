
from django.urls import path
from .views import iniciar_sesion, inicio, registrar
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="inicio"),

    path("login/", iniciar_sesion, name ="login"),
    path("logout/", LogoutView.as_view(template_name="log2/logout.html"), name="logout"),
    path("register/", registrar, name="registrar"),
]
