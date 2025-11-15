# Deployment Configuration for HTTPS

This document provides a sample Nginx configuration for deploying the Django project with HTTPS.

## Nginx Configuration (sample)

This configuration redirects all HTTP traffic to HTTPS and serves the Django application via Gunicorn.

```nginx
# Server block to redirect HTTP to HTTPS
server {
    listen 80;
    server_name your_domain.com;
    return 301 https://$host$request_uri;
}

# Main server block for HTTPS
server {
    listen 443 ssl;
    server_name your_domain.com;

    # Paths to your SSL certificates
    ssl_certificate /etc/letsencrypt/live/your_[domain.com/fullchain.pem](https://domain.com/fullchain.pem);
    ssl_certificate_key /etc/letsencrypt/live/your_[domain.com/privkey.pem](https://domain.com/privkey.pem);

    # Add HSTS header (matches settings.py)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # Serve the Django application
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}