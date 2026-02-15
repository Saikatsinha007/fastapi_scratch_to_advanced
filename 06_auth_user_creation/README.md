# 06_auth_user_creation

A FastAPI + SQLModel authentication module with user signup functionality.

## Features

- User registration (signup)
- User login with JWT token authentication
- Protected routes with OAuth2
- Book management API

## Requirements

- Python 3.8+
- PostgreSQL (or modify for SQLite)

## Installation

```bash
pip install -r requirements.txt
```

## Database Setup

```bash
alembic upgrade head
```

## Running the Application

```bash
uvicorn src.main:app --reload
```

## API Endpoints

### Authentication
- `POST /auth/signup` - Register a new user
- `POST /auth/login` - Login and get access token
- `GET /auth/me` - Get current user info

### Books
- `GET /books` - Get all books
- `GET /books/{id}` - Get a specific book
- `POST /books` - Create a new book
- `PUT /books/{id}` - Update a book
- `DELETE /books/{id}` - Delete a book
