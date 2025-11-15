from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .forms import BookForm

def is_admin(user):
    """Checks if the user is an Admin."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user is a Librarian."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user is a Member."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# 1. Implement Function-based View (FBV)
@permission_required('relationship_app.can_view', login_url='/relations/login/')
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

# 4. Role-Based Views

@login_required
@user_passes_test(is_admin, login_url='/relations/login/') # Redirect non-admins
def admin_view(request):
    # The file name is 'admin_view.html' as requested
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/relations/login/') # Redirect non-librarians
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/relations/login/') # Redirect non-members
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# 4. Role-Based Views

@login_required
@user_passes_test(is_admin, login_url='/relations/login/') # Redirect non-admins
def admin_view(request):
    # The file name is 'admin_view.html' as requested
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/relations/login/') # Redirect non-librarians
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/relations/login/') # Redirect non-members
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# 5. Secured CRUD Views for Books

@permission_required('relationship_app.can_create', login_url='/relations/login/')
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# @permission_required('relationship_app.can_change_book', login_url='/relations/login/')
@permission_required('relationship_app.can_edit', login_url='/relations/login/')
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list-books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# @permission_required('relationship_app.can_delete_book', login_url='/relations/login/')
@permission_required('relationship_app.can_delete', login_url='/relations/login/')
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list-books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})