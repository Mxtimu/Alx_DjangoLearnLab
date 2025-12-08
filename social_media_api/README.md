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
