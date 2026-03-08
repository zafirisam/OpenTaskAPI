#OpenTaskAPI

OpenTaskAPI is a lightweight RESTful task management API built using **FastAPI**, **SQLAlchemy** and **SQLite**.
It is designed to run on bare-metal operating systems (Windows, macOS and Linux) without requiring containers, virtual machines or heavy database servers.
This project demonstrates the design and distribution of a small open-source software artifact.

---

##Features

* Create, read, update and delete tasks (CRUD operations)
* Lightweight SQLite database persistence
* FastAPI framework for high-performance APIs
* Automated testing using pytest
* Interactive API documentation via Swagger UI
* Open-source MIT License

---

##Technology Stack

| Component            | Technology   |
| -------------------- | ------------ |
| Programming Language | Python 3.10+ |
| Web Framework        | FastAPI      |
| Web Server           | Uvicorn      |
| Database             | SQLite       |
| ORM                  | SQLAlchemy   |
| Testing              | pytest       |
| Distribution         | GitHub       |

---

##Project Structure

```
OpenTaskAPI
│
├── app
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
│
├── tests
│   └── test_api.py
│
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

---

##Installation

Clone the repository:

```
git clone https://github.com/yourusername/opentaskapi.git
```

Navigate into the project folder:

```
cd opentaskapi
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment.

###Windows

```
venv\Scripts\activate
```

###macOS / Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt(the are inside the file)
```

---

##Running the API

Start the server using:

```
uvicorn app.main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

##API Endpoints

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| POST   | /tasks           | Create a new task  |
| GET    | /tasks           | Retrieve all tasks |
| PUT    | /tasks/{task_id} | Update a task      |
| DELETE | /tasks/{task_id} | Delete a task      |

Example request:

```
POST /tasks
```

Example JSON body:

```
{
  "title": "Complete assignment",
  "description": "Finish OpenTaskAPI project"
}
```

---

##Running Tests

Run automated tests using:

```
pytest
```

The tests verify that the API endpoints operate correctly.

---

##Database

The application uses **SQLite** for persistence.

A database file will automatically be created when the application runs:

```
tasks.db
```

This allows the API to operate without installing a separate database server.

---

## License

This project is licensed under the **MIT License**.

See the LICENSE file for details.

---

## Contributing

Contributions are welcome.
Please read the **CONTRIBUTING.md** file for guidelines before submitting pull requests or reporting issues.

---

## Author
Zafeirios Samoladas
Developed as part of an academic open-source software engineering project.
