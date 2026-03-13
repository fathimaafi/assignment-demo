# Greeter Project

This is a simple Python project that provides a greeting functionality and demonstrates basic unit testing and linting practices.

## Project Structure

- `greet.py`: Main module containing the greeting logic.
- `test_greet.py`: Unit tests for the greeting functionality.
- `.github/workflows/test.yml`: GitHub Actions configuration for automated linting and testing.
- `requirements.txt`: Project dependencies.

## Features

- Greets a user with a customizable message.
- Full unit test coverage for the greeting function.
- Integrated linting with `pylint` to ensure high code quality.

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd greeter
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   On Windows:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the greeting script manually:
```bash
python greet.py
```

## Running Tests

To run the unit tests:
```bash
python -m unittest discover -p 'test_greet.py'
```

## Linting

### What is Linting?
Linting is the automated process of checking source code for programmatic and stylistic errors. It helps maintain a consistent coding style, catches potential bugs early, and improves overall code readability and maintainability.

### How to Run Linting Locally
This project uses `pylint` for linting. You can run it locally using the following command:
```bash
pylint greet.py test_greet.py
```
*Note: If you are using the virtual environment `myenv` on Windows without activating it, use:*
```bash
myenv\Scripts\pylint.exe greet.py test_greet.py
```

## CI/CD Pipeline
The project is configured with a GitHub Action that automatically runs `pylint` and then executes the unit tests on every push to the `main` branch. This ensures that all code meets the required quality standards and passes all tests before being integrated.
