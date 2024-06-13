from django import forms
from . import models

class BooksForm(forms.ModelForm):
    class Meta:
        model = models.Book_list
        fields = '__all__'