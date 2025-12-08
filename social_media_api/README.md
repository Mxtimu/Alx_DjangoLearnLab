# Social Media API

## Setup
1. Clone repo.
2. Run pip install -r requirements.txt
3. Run python manage.py migrate
4. Run python manage.py runserver

## Authentication
* **Register:** POST /api/users/register/ (Returns Token)
* **Login:** POST /api/users/login/ (Returns Token)
* **Profile:** GET/PUT /api/users/profile/ (Requires Token)

## Posts & Comments
* **List Posts:** GET /api/posts/ (Supports pagination & search: ?search=keyword)
* **Create Post:** POST /api/posts/
* **Post Details:** GET /api/posts/{id}/
* **Update/Delete Post:** PUT/DELETE /api/posts/{id}/ (Author only)
* **Comments:** CRUD operations at /api/comments/
