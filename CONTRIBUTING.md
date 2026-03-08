#Contributing to OpenTaskAPI

Thank you for your interest in contributing to OpenTaskAPI. Contributions help improve the project and make it more useful for the Software enginering community.

---

##How to Contribute

There are several ways to contribute to this project:

* Reporting bugs
* Suggesting new features
* Improving documentation
* Writing tests
* Submitting code improvements

---

##Reporting Issues

If you discover a bug or problem please open an issue on the GitHub repository and include:

* A clear description of the issue
* Steps to reproduce the problem
* Expected vs actual behavior
* Any relevant screenshots or error messages

---

##Development Setup

1. Clone the repository:
```
git clone https://github.com/yourusername/opentaskapi.git
```

2. Navigate into the project directory:
```
cd opentaskapi
```

3. Create a virtual environment:
```
python -m venv venv
```

4. Activate the environment.
Windows:

```
venv\Scripts\activate
```

macOS/Linux:

```
source venv/bin/activate
```

5. Install dependencies:
```
pip install -r requirements.txt
```

---

##Running the Application

Start the API server using:
```
uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

##Running Tests

Before submitting changes please run the test suite:

```
pytest
```

All tests should pass before submitting a pull request.

---

##Pull Request Guidelines

When submitting a pull request:

1. Fork the repository
2. Create a new branch for your feature or fix
3. Write clear commit messages
4. Ensure your code follows Python best practices
5. Make sure tests pass successfully

Example:

```
git checkout -b feature/add-task-priority
```

---

## Code Style

Please follow standard Python style guidelines:

* Follow PEP 8 formatting
* Use descriptive variable and function names
* Write clear and concise comments where necessary

---

##License
By contributing to this project, you agree that your contributions will be licensed under the **MIT License**.
