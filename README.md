# devops_microservices-main

### Containerized Microservices Architecture

This project demonstrates a **microservices-based architecture** using Docker, Flask, Redis, and PostgreSQL. The architecture breaks a monolithic application into independent services that can scale and operate individually. The application includes:

- `user-service`: Handles user-related business logic.
- `data-service`: Manages database operations.
- `Redis`: Caching layer to reduce load on PostgreSQL.
- `PostgreSQL`: Persistent relational database.
- Orchestrated via `Docker Compose`.

---

## 📌 Project Objective

To break a monolithic Python application into lightweight microservices, containerize them, and orchestrate them using Docker Compose for better scalability, modularity, and maintainability.

---

## 🧱 Architecture Overview

```text
+----------------+        +----------------+        +----------------+
|  user-service  |<------>|  data-service  |<------>|   PostgreSQL   |
| (Flask App)    |        | (Flask App)    |        | (Database)     |
+----------------+        +----------------+        +----------------+
        |                          |
        +--------------------------+
                   |
             +-------------+
             |    Redis    |
             +-------------+
```

## 🛠 Tools & Technologies
* Docker & Docker Compose
* Python (Flask)
* Redis
* PostgreSQL
* GitHub
* REST API
* YAML

## 📂 Folder Structure
```text
.
├── user-service
│   ├── app.py
│   └── Dockerfile
├── data-service
│   ├── app.py
│   └── Dockerfile
├── init.sql
├── docker-compose.yml
└── README.md
```

## ⚙️ How to Run the Project
1. Clone the Repository
```text
git clone https://github.com/your-username/containerized-microservices-architecture.git
cd containerized-microservices-architecture
```
2. Launch with Docker Compose
   ```text
   docker-compose up --build
   ```

4. Access Services
   * user-service: http://localhost:5000
   * data-service: http://localhost:5001
   * PostgreSQL and Redis run in the background and support service logic.

## 🔑 Key Highlights
* Broke a monolithic app into modular microservices
* Created individual Dockerfiles for each service
* Implemented Redis to reduce DB load and latency
* Used Docker Compose for full-service orchestration
* Verified communication between services using internal networking

## 📌 Future Improvements
* Add authentication & authorization
* Implement load balancing
* Use Kubernetes for production-level orchestration
* Add health checks and monitoring

## 📬 Contact
Nitin Dhiman
* GitHub - https://github.com/nitindhiman22/
* LinkedIn -https://www.linkedin.com/in/nitin-dhiman22

