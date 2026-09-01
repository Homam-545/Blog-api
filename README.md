# Blog API

A RESTful Blog API built with **Django** and **Django REST Framework (DRF)**, featuring JWT authentication, filtering, and auto-generated API documentation.

## Features

- 📝 CRUD operations for blog posts
- 🔐 JWT authentication (`djangorestframework-simplejwt`)
- 🔍 Filtering & search support (`django-filter`)
- 📖 Auto-generated API docs (`drf-spectacular` — Swagger/OpenAPI)
- 🖼️ Image/media upload support

## Tech Stack

- Python / Django
- Django REST Framework
- Simple JWT (authentication)
- drf-spectacular (OpenAPI schema & docs)
- django-filter

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Homam-545/Blog-api.git
cd Blog-api

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file (see Environment Variables below)

# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser (optional, for admin panel access)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

> Never commit your real `.env` file or `SECRET_KEY` to version control.

## API Documentation

Once the server is running, interactive API docs are available at:

- Swagger UI: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- Redoc: `http://127.0.0.1:8000/api/schema/redoc/`

*(Adjust these paths to match your actual `urls.py` configuration.)*

## API Endpoints

| Method | Endpoint                | Description                  | Auth Required |
|--------|--------------------------|-------------------------------|:---:|
| POST   | `/api/token/`             | Obtain JWT access/refresh token | No |
| POST   | `/api/token/refresh/`     | Refresh JWT access token       | No |
| GET    | `/api/posts/`             | List all blog posts            | No |
| POST   | `/api/posts/`             | Create a new post               | Yes |
| GET    | `/api/posts/{id}/`        | Retrieve a single post          | No |
| PUT    | `/api/posts/{id}/`        | Update a post                   | Yes |
| DELETE | `/api/posts/{id}/`        | Delete a post                   | Yes |

## Project Structure

```
Blog-api/
├── BlogSystem/       # Django project settings
├── core/             # Main app (models, views, serializers)
├── media/images/     # Uploaded media files
├── manage.py
└── requirements.txt
