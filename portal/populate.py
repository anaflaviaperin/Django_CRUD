from portal.models import Categoria, Autor, Livro
from datetime import date

def run():
    categoria1 = Categoria.objects.create(nome="Ficção Científica")
    categoria2 = Categoria.objects.create(nome="Biografia")
    categoria3 = Categoria.objects.create(nome="Autoajuda")
    categoria4 = Categoria.objects.create(nome="História")
    categoria5 = Categoria.objects.create(nome="Tecnologia")

    autor1 = Autor.objects.create(nome="Isaac Asimov", data_nascimento=date(1920, 1, 2))
    autor2 = Autor.objects.create(nome="Walter Isaacson", data_nascimento=date(1952, 5, 20))
    autor3 = Autor.objects.create(nome="Dale Carnegie", data_nascimento=date(1888, 11, 24))
    autor4 = Autor.objects.create(nome="Yuval Noah Harari", data_nascimento=date(1976, 2, 24))
    autor5 = Autor.objects.create(nome="Eric S. Raymond", data_nascimento=date(1957, 12, 4))

    livro1 = Livro.objects.create(titulo="Fundação", autor=autor1, categoria=categoria1, numeropaginas=255)
    livro2 = Livro.objects.create(titulo="Steve Jobs", autor=autor2, categoria=categoria2, numeropaginas=656)
    livro3 = Livro.objects.create(titulo="Como Fazer Amigos e Influenciar Pessoas", autor=autor3, categoria=categoria3, numeropaginas=291)
    livro4 = Livro.objects.create(titulo="Sapiens: Uma Breve História da Humanidade", autor=autor4, categoria=categoria4, numeropaginas=443)
    livro5 = Livro.objects.create(titulo="A Catedral e o Bazar", autor=autor5, categoria=categoria5, numeropaginas=241)