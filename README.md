[![Run Tests](https://github.com/fathimaafi/assignment-demo/actions/workflows/test.yml/badge.svg)](https://github.com/fathimaafi/assignment-demo/actions/workflows/test.yml)

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

## Triggering the Workflow Manually

In addition to automatic runs on push, the workflow can be triggered manually using `workflow_dispatch`:

1. Go to your repository on [GitHub](https://github.com).
2. Click the **Actions** tab.
3. Select **Run Tests** from the left sidebar.
4. Click the **Run workflow** dropdown on the right.
5. Choose the branch (e.g., `main`) and click **Run workflow**.

The workflow will start within a few seconds and you can monitor its progress in the Actions tab.

## Accessing Test Artifacts

After each workflow run, the verbose test results are saved and uploaded as a downloadable artifact named `test-results`.

### How to Access

1. Go to your repository on [GitHub](https://github.com).
2. Click the **Actions** tab.
3. Select the workflow run you want to inspect.
4. Scroll down to the **Artifacts** section at the bottom of the run summary page.
5. Click **test-results** to download the zip file.
6. Extract the zip and open `test-results.txt` to view the full verbose test output.

### What the Artifact Contains

- Each test method name with its pass (`ok`) or fail (`FAIL`) status
- Total number of tests run, failures, and errors
- Full traceback for any failed tests

Example output:
```
test_empty_string (test_greet.TestGreet) ... ok
test_valid_name (test_greet.TestGreet) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

> Note: Artifacts are available for 90 days by default after which GitHub automatically deletes them.
