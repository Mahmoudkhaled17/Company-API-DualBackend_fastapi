# Company Management API (FastAPI & PostgreSQL)

A high-performance, asynchronous RESTful API built to demonstrate advanced Python backend engineering, structured database modeling, and automated data serialization workflows. This project serves as a standalone backend for a modern corporate management pipeline.

---

## 🏗️ Relational Database Design

The database is built on a highly normalized relational structure handling departments, employee rosters, specialized course tracking, and student performance metrics.

### Database Schema (ER Diagram)
<img width="1312" height="777" alt="Screenshot 2026-06-08 232114" src="https://github.com/user-attachments/assets/9b40106e-3ed1-4dae-8067-d9fe2fe8bf50" />

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
<img width="1915" height="950" alt="Screenshot 2026-06-08 232338" src="https://github.com/user-attachments/assets/eb908ad6-0f2b-4476-82e6-2f684a7084f5" />

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
