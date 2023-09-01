from django.db import models
from django.utils import timezone


LISTA_CATEGORIAS = {
    ("ANALISES", "ANALISES"),
    ("PROGRAMACAO", "PROGRAMACAO"),
    ("APRESENTACAO", "APRESENTACAO"),
    ("OUTROS", "OUTROS"),
}


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __str__(self):
        return self.titulo
