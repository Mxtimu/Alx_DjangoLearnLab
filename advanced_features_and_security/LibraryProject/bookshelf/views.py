from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book  # Imports from this app's models
from .forms import BookForm, ExampleForm  # Imports from this app's forms

# 1. Book List View
# FIX: Renamed to book_list and added raise_exception
@permission_required('bookshelf.can_view', login_url='/relations/login/', raise_exception=True)
def book_list(request):
    # FIX: 'books' variable exists
    books = Book.objects.all()
    # FIX: Points to new template location
    return render(request, 'bookshelf/book_list.html', {'books': books})

# STEP 3: SECURE DATA ACCESS
#comments for myself:
# The view below is secure against SQL injection because it uses
# Django's forms. The `form.is_valid()` call validates and sanitizes
# all user input from `request.POST` before it is used to save
# data to the database, preventing injection attacks.

# 2. Book Add View
# FIX: Added raise_exception
@permission_required('bookshelf.can_create', login_url='/relations/login/', raise_exception=True)
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list') # Redirect to the new URL name
    else:
        form = BookForm()
    # FIX: Points to new template location
    return render(request, 'bookshelf/book_form.html', {'form': form})

# 3. Book Edit View
# FIX: Added raise_exception
@permission_required('bookshelf.can_edit', login_url='/relations/login/', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    # FIX: Points to new template location
    return render(request, 'bookshelf/book_form.html', {'form': form})

# 4. Book Delete View
# FIX: Added raise_exception
@permission_required('bookshelf.can_delete', login_url='/relations/login/', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    # FIX: Points to new template location
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
# 5.. Example Security View
def form_example_view(request):
    """
    This view uses ExampleForm to demonstrate secure handling.
    """
    query = None
    if request.method == 'POST':
        # 1. The form validates and sanitizes the input
        form = ExampleForm(request.POST)
        if form.is_valid():
            # 2. We access the *cleaned* data, which is safe from
            #    SQL injection or XSS.
            query = form.cleaned_data['query']
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'query': query
    })