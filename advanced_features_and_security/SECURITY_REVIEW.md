# Security Review Report

This document details the security measures implemented in the application.

## 1. HTTPS Enforcement (settings.py)

* `SECURE_SSL_REDIRECT = True`: All HTTP traffic is forcibly redirected to HTTPS.
* `SECURE_HSTS_SECONDS = 31536000`: HSTS is enabled for one year, forcing browsers to use HTTPS after their first visit.
* `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: The HSTS policy is applied to all subdomains.
* `SECURE_HSTS_PRELOAD = True`: Allows the site to be submitted to browser HSTS preload lists for maximum security.

## 2. Secure Cookies (settings.py)

* `SESSION_COOKIE_SECURE = True`: Session cookies will only be sent over HTTPS.
* `CSRF_COOKIE_SECURE = True`: CSRF cookies will only be sent over HTTPS.

## 3. Secure Headers (settings.py)

* `X_FRAME_OPTIONS = 'DENY'`: Prevents the site from being used in an `<iframe>`, mitigating clickjacking attacks.
* `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents the browser from guessing file types, which stops certain XSS attacks.
* `SECURE_BROWSER_XSS_FILTER = True`: Enables the browser's built-in XSS filter.

## 4. Content Security Policy (CSP)

* `django-csp` is installed and configured to only allow scripts and styles from trusted domains (`'self'` and specific CDNs), which is a primary defense against XSS.

## 5. Application-Level Security

* **CSRF Tokens**: All forms use `{% csrf_token %}`.
* **SQL Injection**: All database queries use the Django ORM and Django Forms, which parameterize queries and prevent SQL injection.
* **Permissions**: Views are protected with `@permission_required` decorators to ensure only authorized users can perform actions.