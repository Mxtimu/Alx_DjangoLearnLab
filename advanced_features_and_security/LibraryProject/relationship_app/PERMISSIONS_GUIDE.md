# Permissions and Groups Setup

This document explains the custom permissions and the recommended group setup.

## 1. Custom Permissions (models.py)

The Book model in elationship_app has the following custom permissions:

* elationship_app.can_view: Allows user to see the list of books.
* elationship_app.can_create: Allows user to add a new book.
* elationship_app.can_edit: Allows user to edit an existing book.
* elationship_app.can_delete: Allows user to delete a book.

## 2. Group Setup (Manual Admin Task)

To use these permissions, create groups in the Django Admin (/admin/auth/group/add/).

1.  **Create a 'Viewers' Group:**
    * Go to the admin site, click 'Groups', then 'Add Group'.
    * Name: Viewers
    * Permissions: Select elationship_app | book | Can view book.

2.  **Create an 'Editors' Group:**
    * Name: Editors
    * Permissions:
        * elationship_app | book | Can view book
        * elationship_app | book | Can create book
        * elationship_app | book | Can edit book

3.  **Create an 'Admins' Group:**
    * Name: Admins
    * Permissions: Select all permissions for the elationship_app | book.

## 3. Assigning Users

Go to the User admin page, select a user, and assign them to one of these groups (e.g., 'Editors') to grant them the permissions.
