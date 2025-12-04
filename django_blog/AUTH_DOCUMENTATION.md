# Authentication System Documentation

## Overview
The authentication system allows users to register, login, logout, and manage their profile (email).

## Components

### 1. Forms (forms.py)
* CustomUserCreationForm: Extends Django's default creation form to include an 'email' field.
* UserUpdateForm: Allows authenticated users to update their email address.

### 2. Views (views.py)
* egister: Handles user creation and automatic login upon success.
* profile: Protected by @login_required. Displays user info and handles profile updates.
* LoginView / LogoutView: Built-in Django views used in urls.py.

### 3. Templates
* login.html, logout.html, egister.html: Standard forms using CSRF tokens.
* profile.html: Displays user data and an update form.

## How to Test
1. **Register**: Go to /register/. Create a user. You should be redirected to /profile/.
2. **Profile**: Change your email on /profile/ and click Update.
3. **Logout**: Click Logout. You should see the logout confirmation.
4. **Login**: Go to /login/ and enter your credentials.
