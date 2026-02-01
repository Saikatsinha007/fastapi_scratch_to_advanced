

# FastAPI End-to-End Guide with Explanations

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Starting the FastAPI Server](#starting-the-fastapi-server)
4. [Endpoints Explained](#endpoints-explained)

   * Root Endpoint
   * Query Parameters
   * Optional Parameters
   * Request Body (POST)
   * Request Headers
5. [Testing Endpoints](#testing-endpoints)
6. [Swagger UI & Documentation](#swagger-ui--documentation)
7. [Common Issues & Troubleshooting](#common-issues--troubleshooting)
8. [Next Steps](#next-steps)

---

## Introduction

FastAPI is a modern, fast Python framework for building APIs. It automatically handles:

* Data validation with **Pydantic models**
* Interactive API documentation
* Type hints for better developer experience

This guide walks through **everything from scratch**, including endpoints, request body, headers, optional parameters, and testing.

---

## Setup

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Optional (if using extra Pydantic validation):

```bash
pip install pydantic
```

3. Create your main file, e.g., `04_request_body.py`.

---

## Starting the FastAPI Server

```bash
uvicorn 04_request_body:app --reload
```

* `04_request_body` → filename without `.py`
* `app` → FastAPI instance
* `--reload` → automatically reloads when the file changes

Server runs at:

```
http://127.0.0.1:8000
```

---

## Endpoints Explained

### 1. Root Endpoint

```python
@app.get("/")
async def root():
    return {"message": "FastAPI is running 🚀"}
```

**Explanation:**

* **`@app.get("/")`** → Registers a GET route at the root `/`.
* **`async def root()`** → Async function to handle the request.
* **Return value** → FastAPI converts Python dictionary to JSON automatically.
* **Why:** Provides a simple health check to ensure the server is running.

---

### 2. Query Parameters (Required)

```python
@app.get("/search")
async def search_for_user(username: str):
    if username in user_list:
        return {"message": f"Details for user {username}"}
    raise HTTPException(status_code=404, detail="User Not Found")
```

**Explanation:**

* `username: str` → Query parameter because it’s not in the path.
* FastAPI **automatically validates** that `username` is provided.
* If user exists → return details
* If user not found → raise **404 HTTPException**
* **Why:** Query parameters are used to filter/search resources.

**Test URL:**

```
http://127.0.0.1:8000/search?username=Jerry
```

---

### 3. Optional Query Parameters

```python
from typing import Optional

@app.get("/greet/")
async def greet(username: Optional[str] = "User"):
    return {"message": f"Hello {username}"}
```

**Explanation:**

* `Optional[str] = "User"` → Makes the query parameter optional.
* If user provides a value → use it.
* If not → defaults to `"User"`.
* **Why:** Allows flexible endpoints that don’t require all parameters.

**Examples:**

```
/greet/ → Hello User
/greet/?username=Phil → Hello Phil
```

---

### 4. Request Body (POST)

```python
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str

@app.post("/create_user")
async def create_user(user_data: UserSchema):
    new_user = {"username": user_data.username, "email": user_data.email}
    users.append(new_user)
    return {"message": "User created successfully", "user": new_user}
```

**Explanation:**

* **`BaseModel`** → Defines structure of expected JSON.
* **`user_data: UserSchema`** → FastAPI automatically parses JSON body into `UserSchema`.
* Missing fields → **422 Unprocessable Entity**
* **Why:** Using Pydantic ensures data integrity and automatic validation.

**Testing:**

* Valid JSON → returns `200 OK` with user info
* Missing field → `422`

---

### 5. Request Headers

```python
from fastapi import Header
from typing import Optional

@app.get("/get_headers")
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    return {
        "User-Agent": user_agent,
        "Accept-Encoding": accept_encoding,
        "Referer": referer,
        "Accept-Language": accept_language,
        "Connection": connection,
        "Host": host
    }
```

**Explanation:**

* `Header(None)` → Optional header parameter
* FastAPI automatically maps **HTTP headers** (snake_case) to Python variables.
* Returns dictionary of headers.
* **Why:** Sometimes endpoints need context (user agent, language, host, etc.).

**Testing:**

* Swagger UI or curl will show actual headers your browser/client sends.

---

## Testing Endpoints

### 1. Swagger UI (Recommended)

* Open: `http://127.0.0.1:8000/docs`
* Click endpoint → **Try it out** → Fill parameters or JSON → **Execute**
* See response, status code, headers instantly

### 2. Curl

**POST /create_user**

```bash
curl -X POST "http://127.0.0.1:8000/create_user" \
-H "Content-Type: application/json" \
-d '{"username":"Jerry","email":"jerry@example.com"}'
```

**GET /search**

```bash
curl "http://127.0.0.1:8000/search?username=Jerry"
```

---

## Swagger UI & Documentation

* Auto-generated at `/docs`
* Shows endpoint methods, parameters, request body schemas
* Shows expected responses and validation errors
* Optional: `/redoc` provides a cleaner layout

---

## Common Issues & Troubleshooting

| Issue                            | Cause                                                             | Fix                                                            |
| -------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| 404 Not Found                    | Accessing a route that doesn’t exist or server running wrong file | Add route or run correct file: `uvicorn filename:app --reload` |
| 422 Unprocessable Entity         | Missing JSON body or required fields in POST                      | Provide all required fields                                    |
| Swagger UI doesn’t show endpoint | Server running wrong file                                         | Save file & restart uvicorn                                    |
| ReqBin asks for extension        | Trying to test local server (`127.0.0.1`) online                  | Use Swagger UI or curl locally                                 |

---

## Next Steps / Learning Path

* Path parameters vs query parameters
* Optional + default values
* PUT / PATCH requests
* Full CRUD API
* Validation rules (`min_length`, `EmailStr`, regex)
* Dependency injection (`Depends`)
* Authentication and Authorization

---

## References

* [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

