from django.shortcuts import render, redirect

from portal.forms import AutorForms, CategoriaForms, LivroForms
from portal.models import Autor, Categoria, Livro


# Create your views here.
def home(request):
    return render(request, 'portal/home.html')

def autor(request):
    autores = Autor.objects.all()

    dicautores = {
        'autores': autores
    }

    return render(request, 'portal/autores.html', dicautores)

def autoradicionar(request):
    form = AutorForms(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autores')

    context = {
        'form': form
    }

    return render(request, 'portal/autoradd.html', context)

def autoredit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForms(request.POST or None, instance=autor)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autores')

    context = {
        'form': form,
        'autor': autor
    }

    return render(request, 'portal/autoredit.html', context)

def autordelete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()

    return redirect('autores')

def categorias(request):
    categorias = Categoria.objects.all()

    dicCategorias = {
        'categorias': categorias
    }

    return render(request, 'portal/categorias.html', dicCategorias)

def categoriaAdicionar(request):
    form = CategoriaForms(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categorias')

    dicCategorias = {
        'form' : form
    }

    return render(request, 'portal/categoriaadd.html', dicCategorias)

def categoriaEditar(request, categoria_pk):
    categoria = Categoria.objects.get(pk=categoria_pk)

    form = CategoriaForms(request.POST or None, instance=categoria)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categorias')

    dicCategorias = {
        'form': form,
        'categoria': categoria
    }

    return render(request, 'portal/categoriaedit.html', dicCategorias)

def categoriaExcluir(request, categoria_pk):
    categoria = Categoria.objects.get(pk=categoria_pk)
    categoria.delete()

    return redirect('categorias')

def livros(request):
    livros = Livro.objects.all()

    dicLivros = {
        'livros': livros
    }

    return render(request, 'portal/livros.html', dicLivros)


def livroAdicionar(request):
    form = LivroForms(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livros')

    dicLivros = {
        'form': form
    }

    return render(request, 'portal/livroadd.html', dicLivros)

def livroEditar(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    form = LivroForms(request.POST or None, instance=livro)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livros')

    dicLivros = {
        'form': form,
        'livro': livro
    }

    return render(request, 'portal/livroedit.html', dicLivros)

def livroExcluir (request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()

    return redirect('livros')