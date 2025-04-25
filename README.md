# 🧬 DNA Sequence API

A Python-based web service that stores and retrieves randomly generated DNA sequences using FastAPI, PostgreSQL, and SQLAlchemy.

---

## 🚀 Features

- Generate and store random DNA sequences composed of A, C, G, T
- Retrieve all stored DNA sequences via REST API
- Persistent PostgreSQL database
- Automated testing via GitHub Actions

---

## 🧰 Requirements

- Python 3.8 or higher
- PostgreSQL installed and running
- Recommended: Use a virtual environment

Dependencies are listed in `requirements.txt`.

---

## 🗃️ PostgreSQL Setup

1. Create the database named `dna_sequences` in PostgreSQL.
2. Use the default credentials:
   - **Username**: `postgres`
   - **Password**: `postgres`
3. Ensure that your Python code references this database using a connection string.

---

## 📁 Project Structure

- `main.py`: FastAPI entrypoint containing routes for generating and retrieving DNA sequences.
- `models.py`: SQLAlchemy ORM model for the DNA sequence table.
- `database.py`: Configuration for the PostgreSQL connection and session management.
- `utils.py`: Contains the logic to randomly generate DNA sequences.
- `requirements.txt`: Lists all Python dependencies required to run the app.
- `.github/workflows/python-app.yml`: GitHub Actions workflow for CI/CD.

---

## 🚀 Running the App

1. Install dependencies using `pip install -r requirements.txt`
2. Ensure PostgreSQL is running and the database is accessible.
3. Start the API with a command like `uvicorn main:app --reload`
4. Access the interactive API docs at `http://localhost:8000/docs`

---

## 📬 API Endpoints

- `POST /generate/?name=...`  
  Creates and stores a new randomly generated DNA sequence associated with the given name.

- `GET /sequences/`  
  Returns a list of all stored DNA sequences from the database.

---

## 🧪 Continuous Integration

This project uses **GitHub Actions** to run tests automatically on pushes and pull requests to the `main` branch.

The CI workflow:

- Starts a PostgreSQL 13 service
- Installs project dependencies
- Waits for the database to be ready
- Runs all Python tests using `pytest`

Configuration is stored in `.github/workflows/python-app.yml`.

---

## ✅ Future Enhancements

- Add support for filtering sequences by name or pattern
- Implement pagination for large datasets
- Add user authentication and access control
- Improve test coverage and add integration tests

---
