## **Task 1: User Management API (Foundation Task)**

### **Objective**

Build a secure CRUD API for users.

### **Requirements**

- **FastAPI** for endpoints
- **PostgreSQL** as DB
- **SQLAlchemy ORM**
- **Pydantic** for validation

### **Endpoints**

- `POST /users` – Create user
- `GET /users/{id}` – Get user by ID
- `GET /users` – List users (pagination)
- `PUT /users/{id}` – Update user
- `DELETE /users/{id}` – Soft delete user

### **Validation Rules**

- Email must be valid and unique
- Password min length: 8
- Name cannot be empty
- Age must be >= 18

##