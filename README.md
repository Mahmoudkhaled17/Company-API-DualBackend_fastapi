# Company Management API (FastAPI & PostgreSQL)

A high-performance, asynchronous RESTful API built to demonstrate advanced Python backend engineering, structured database modeling, and automated data serialization workflows. This project serves as a standalone backend for a modern corporate management pipeline.

---

## 🏗️ Relational Database Design

The database is built on a highly normalized relational structure handling departments, employee rosters, specialized course tracking, and student performance metrics.

### Database Schema (ER Diagram)
*Replace this text with your dBeaver ER Diagram screenshot!*

### Key Architecture Details:
- **Many-to-Many Bridge Table (`CrsResults`)**: Seamlessly connects `Courses` and `Trainees` to maintain strict relational integrity for tracking scores.
- **Foreign Key Constraints**: Formulated with explicit `ondelete='NO ACTION'` behaviors to preserve structural coupling without cascade anomalies.

---

## 🛠️ Tech Stack & Features

- **Core Framework:** FastAPI (Asynchronous ASGI server ecosystem)
- **ORM / Database Driver:** SQLAlchemy (Core & Declarative ORM mapping)
- **Data Serialization & Transfer Layer:** Pydantic v2
- **Database Engine:** PostgreSQL

### 🌟 Advanced Feature: Decoupled Pydantic Schemas & DTO Aliasing
To separate database internals from client-facing API responses, this system implements Pydantic `validation_alias` and `from_attributes=True`. It reads PascalCase columns directly from the database (`Id`, `Name`, `Address`) and automatically serializes them into standard clean camel_case / snake_case response blocks (`instructor_id`, `instructor_name`).

---

## 📬 API Contract & Live Preview

### Endpoint: `GET /instructors`
Retrieves all certified trainers inside the enterprise along with their departmental metadata.

### Swagger UI Execution Screenshot
*Take a screenshot of your FastAPI Swagger UI output response body and place it here!*

### Sample JSON Output (DTO Format)
```json
[
  {
    "instructor_id": 1,
    "instructor_name": "Dr. Mahmoud Khaled",
    "instructor_image_url": "mahmoud_avatar.jpg",
    "instructor_address": "Smart Village, Egypt",
    "instructor_salary": "15000"
  }
]