from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    numeropaginas = models.PositiveIntegerField("Número de Páginas")

