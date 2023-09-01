from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Filme
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


def homepage(request):
    
    contexto = {
        "titulo": 'Bem-Vindo ao AxoFlix'
    }
    return render(request, "homepage.html",contexto)


def lista_curso(request):
    usuario = User.objects.all().first
    filme = Filme.objects.all()
    contexto = {"filme": filme,
                "usuario": usuario,
                "titulo": 'Todos os Cursos'}
    return render(request, "lista_curso.html", contexto)


def consulta(request):
    # Obtém o valor de busca da query string 'q' na URL
    search_value = request.GET.get("q", "").strip()
    print(search_value)

    if search_value == "":
        # Se a busca estiver vazia, redirecione para outra página
        return redirect("filme:lista_curso")
    
    # Realize a consulta ao banco de dados usando o objeto Filme e a busca fornecida
    filme = Filme.objects.filter(
        Q(titulo__icontains=search_value)
        | Q(descricao__icontains=search_value)
        | Q(categoria__icontains=search_value)
        | Q(data_criacao__icontains=search_value)
    ).order_by("-id")

    # Crie um contexto com os resultados da consulta
    contexto = {
        "filme": filme  # Use "filmes" em vez de "consulta"
    }
    return render(request, "lista_curso.html", contexto)