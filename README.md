# Task Management Application (Full Stack)

A full-stack To-Do application built with a FastAPI backend, a MySQL database, and a React (Vite) frontend.

This project is fully containerized. Using Docker Compose, the frontend, backend, and database are orchestrated to spin up simultaneously with a single command.

---

### 🏗 Tech Stack

- **Database:** MySQL (Dockerized)
- **Backend:** Python / FastAPI / SQLAlchemy (Dockerized)
- **Frontend:** React / Vite / CSS (Dockerized)
- **Testing:** Pytest (Backend) & Vitest (Frontend UI)

---

## 📂 Project Structure & File Guide

```text
to-do-app/
├── backend/
│   ├── main.py
│   ├── dependencies.py
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routers/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
├── .env
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Prerequisites

Before running the application, ensure you have the following installed on your machine:

- **Docker:** [Docker Install Documentation](https://docs.docker.com/engine/install/)

---

## 🚀 Quick Start Guide

**Step 1: Clone the Repository**

Open your terminal and clone this repository to your local machine:

```text
git clone https://github.com/chamzz99/todo-list
cd todo-list
```

**Step 2: Environment Setup (Optional)**

This application is configured to with zero configuration.

If you would like to secure the database or change its name, create a `.env` file (following the `env_sample`) in the root directory:

```text
MYSQL_ROOT_PASSWORD=your_secret_here
MYSQL_DATABASE=your_database_name
```

If no `.env` file is provided, the application will safely default to an empty root password and a database named `tododb`.

**Step 3: Start the Application**

Open your terminal at the root of the project (where the `docker compose.yml` file is located) and run:

```text
docker compose up --build
```

Docker will pull the MySQL image, build the backend and frontend images, and start the network. (Note: The backend will wait until the database reports as healthy before starting).

**Step 4: Access the Application**

Once the terminal logs indicate the services are running, you can access the application here:

- **Frontend UI:** `http://localhost:8080`
- **Backend API (Swagger Docs):** `http://localhost:8000/docs`

---

## 🛑 Stopping the Application

To stop the application and gracefully shut down the containers, press Ctrl+C in the terminal where it is running, or execute:

```text
docker compose down
```

(To wipe the database volume and start completely fresh next time, use `docker compose down -v`)

---
