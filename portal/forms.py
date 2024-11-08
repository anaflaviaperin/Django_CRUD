from django import forms

from portal.models import Autor, Categoria, Livro


class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'data_nascimento')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'})
        }

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''})
        }

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'categoria', 'numeropaginas')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'auto-focus': ''}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'auto-focus': ''}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'auto-focus': ''}),
            'numeropaginas': forms.NumberInput(attrs={'class': 'form-control', 'auto-focus': ''})
        }