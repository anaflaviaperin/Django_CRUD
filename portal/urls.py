from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.autor, name='autores'),
    path('autor/add/', views.autoradicionar, name='autoradd'),
    path('autor/edit/<int:autor_pk>', views.autoredit, name='autoredit'),
    path('autor/delete/<int:autor_pk>', views.autordelete, name='autordelete'),

    path('categorias/', views.categorias, name='categorias'),
    path('categoria/add/', views.categoriaAdicionar, name='categoriaadd'),
    path('categoria/edit/<int:categoria_pk>', views.categoriaEditar, name='categoriaedit'),
    path('categoria/delete/<int:categoria_pk>', views.categoriaExcluir, name='categoriadelete'),

    path('livros/', views.livros, name='livros'),
    path('livro/add/', views.livroAdicionar, name='livroadd'),
    path('livro/edit/<int:livro_pk>', views.livroEditar, name='livroedit'),
    path('livro/delete/<int:livro_pk>', views.livroExcluir, name='livrodelete')

]