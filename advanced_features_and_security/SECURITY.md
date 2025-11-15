# Security Measures Implemented

This document details the security measures implemented in this project.

## 1. settings.py Configuration

* DEBUG = False: Turned off debug mode for production.
* SECURE_BROWSER_XSS_FILTER = True: Enforces XSS filter in browsers.
* X_FRAME_OPTIONS = 'DENY': Prevents clickjacking.
* SECURE_CONTENT_TYPE_NOSNIFF = True: Prevents MIME-type sniffing.
* CSRF_COOKIE_SECURE = True: Enforces CSRF cookies over HTTPS.
* SESSION_COOKIE_SECURE = True: Enforces session cookies over HTTPS.

## 2. CSRF Protection

All forms (login, register, book_form, book_confirm_delete) use the {% csrf_token %} template tag to prevent Cross-Site Request Forgery.

## 3. SQL Injection Protection

All database operations are handled by the Django ORM and Django Forms. Views like ook_add and ook_edit use orm.is_valid() to validate and sanitize user input, which inherently prevents SQL injection attacks.

## 4. Content Security Policy (CSP)

django-csp is installed and configured in settings.py to only allow scripts and styles from our own domain ('self') and trusted CDNs.
