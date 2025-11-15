from django.contrib import admin
from .models import Book  


class BookAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'author', 'publication_year')

    
    search_fields = ('title', 'author')

  
    list_filter = ('publication_year', 'author')


admin.site.register(Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Step 4: Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the admin display
    # This adds them to the "edit" page
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    # This adds them to the "add user" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

# Register your CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)


