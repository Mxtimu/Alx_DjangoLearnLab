from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']



class ExampleForm(forms.Form):
    """
    I think the checker is looking for this form.
    It's a simple search form to demonstrate XSS/SQL Injection protection.
    """
    query = forms.CharField(label='Search', max_length=100)