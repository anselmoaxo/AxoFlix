from django.urls import path, include
from filme import views

app_name = "filme"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lista_curso", views.lista_curso, name="lista_curso"),
    path("consulta/", views.consulta, name="consulta"),
]
