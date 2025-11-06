from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login





# 1. Implement Function-based View (FBV)
def list_books(request):
    """
    Lists all books stored in the database.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# 2. Implement Class-based View (CBV)
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library (by its Primary Key).
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# 3. View for User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # --- FIX: Manually log the user in ---
            user = form.save()  # Save the form and get the new user object
            login(request, user)  # Log the new user in
            # Now redirect to the login redirect URL
            return redirect('list-books')  # Or LOGIN_REDIRECT_URL
            # -----------------------------------
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})