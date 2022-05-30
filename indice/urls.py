
from django.urls import path
from .views import iniciar_sesion, inicio, registrar, editar_user, about_me, info_user, accounts
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", inicio, name="inicio"),

    path("accounts/login/", iniciar_sesion, name ="login"),
    path("accounts/logout/", LogoutView.as_view(template_name="log2/logout.html"), name="logout"),
    path("accounts/signup/", registrar, name="registrar"),
    path("accounts/profile/information", info_user, name="info_user"),
    path("accounts/profile/edite/", editar_user, name="editar_user"),
    path("accounts/profile", accounts, name="accounts"),

    path("about/", about_me, name="about"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)