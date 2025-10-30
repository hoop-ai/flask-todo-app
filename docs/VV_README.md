# Flask Todo App - V&V Project Setup Guide

Complete guide for running the Verification & Validation test suite for the Flask Todo application.

---

## Quick Start (TL;DR)

```bash
# 1. Ensure you're in the flask-todo-app directory
cd flask-todo-app

# 2. Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 3. Start Flask server in one terminal
python app.py

# 4. In another terminal, run all tests
make all
# OR manually:
pytest -v
coverage run -m pytest
coverage report -m
coverage html
crosshair check domain_contracts.py
```

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Running Tests](#running-tests)
5. [Test Suite Overview](#test-suite-overview)
6. [Viewing Results](#viewing-results)
7. [Makefile Commands](#makefile-commands)
8. [Troubleshooting](#troubleshooting)
9. [Project Structure](#project-structure)
10. [Deliverables](#deliverables)

---

## Prerequisites

- **Python 3.12+** (tested with 3.12.10)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Modern web browser** (Chrome, Firefox, or Safari for Playwright)

### Platform Notes

- **Windows:** Commands use `.venv\Scripts\` for virtual environment
- **macOS/Linux:** Commands use `.venv/bin/` for virtual environment

---

## Installation

### Step 1: Navigate to Project Directory

If you don't have the repository yet:

```bash
cd "C:\Users\User\OneDrive\Downloads\Uni\Project - Software Validation\Tasks\flask-todo-app"
```

### Step 2: Verify Virtual Environment Exists

The virtual environment should already be set up. Verify:

```bash
# Windows
.venv\Scripts\python.exe --version
# Should output: Python 3.12.10

# macOS/Linux
# .venv/bin/python --version
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

After activation, your prompt should show `(.venv)` prefix.

### Step 4: Verify Dependencies

All dependencies should already be installed. Verify:

```bash
pip list | grep -E "(pytest|hypothesis|coverage|playwright|icontract|crosshair|Flask)"
```

If any are missing, reinstall:

```bash
pip install -r requirements.txt
pip install pytest hypothesis coverage icontract crosshair-tool playwright pytest-playwright
python -m playwright install
```

---

## Running the Application

### Start Flask Server

Open **Terminal A** and run:

```bash
python app.py
```

You should see:

```
* Serving Flask app "app" (lazy loading)
* Environment: production
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

**Access Points:**
- **Web UI:** http://127.0.0.1:5000
- **Swagger API Docs:** http://127.0.0.1:5000/apidocs
- **API Endpoint:** http://127.0.0.1:5000/api/todos

**Keep this terminal running** while you execute tests in another terminal.

---

## Running Tests

### All Tests at Once (Recommended)

Open **Terminal B** (with Flask still running in Terminal A):

```bash
make all
```

This runs:
1. Pytest test suite
2. Coverage analysis
3. JUnit XML generation
4. CrossHair formal verification

### Individual Test Commands

#### 1. Run All Pytest Tests

```bash
pytest -v
```

**Expected Output:**
```
============================= test session starts =============================
collected 5 items

tests/test_api_properties.py::test_home_ui_loads PASSED                  [ 20%]
tests/test_api_properties.py::test_create_list_roundtrip PASSED          [ 40%]
tests/test_api_properties.py::test_negative_inputs FAILED                [ 60%]
tests/test_contracts.py::test_contract_smoke PASSED                      [ 80%]
tests/test_ui_playwright.py::test_add_todo_and_screenshot PASSED         [100%]

==================== 1 failed, 4 passed in XX.XXs ==========================
```

**Note:** The `test_negative_inputs` failure is expected—it identified a bug (missing title length validation).

#### 2. Run Specific Test Files

```bash
# Functional + property-based tests only
pytest tests/test_api_properties.py -v

# Contract tests only
pytest tests/test_contracts.py -v

# UI tests only (slower, requires Flask running)
pytest tests/test_ui_playwright.py -v
```

#### 3. Generate Coverage Report

```bash
# Run tests with coverage
coverage run -m pytest

# View terminal summary
coverage report -m

# Generate XML for CI/CD
coverage xml -o artifacts/coverage.xml

# Generate HTML report
coverage html
```

**Expected Terminal Output:**
```
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
app.py                            95     45    53%   [lines]
conftest.py                        4      0   100%
domain_contracts.py                6      0   100%
tests\test_api_properties.py      28      0   100%
tests\test_contracts.py            3      0   100%
------------------------------------------------------------
TOTAL                            136     45    67%
```

#### 4. Run Formal Verification

```bash
crosshair check domain_contracts.py
```

**Expected Output:**
```
(no output = success)
```

If CrossHair finds a contract violation, it will output a counterexample.

#### 5. Generate JUnit XML

```bash
pytest --junitxml=artifacts/junit.xml
```

This creates a `junit.xml` file in the `artifacts/` directory for CI/CD integration.

---

## Test Suite Overview

### Test Files

| File | Purpose | Test Count | Coverage |
|------|---------|------------|----------|
| `tests/test_api_properties.py` | Functional + property-based tests for API | 3 tests (100+ Hypothesis cases) | API endpoints |
| `tests/test_contracts.py` | Runtime contract verification | 1 test | Business logic |
| `tests/test_ui_playwright.py` | End-to-end UI testing with browser automation | 1 test | Full UI workflow |
| `domain_contracts.py` | Business rule contracts (used by CrossHair) | N/A | Contract definitions |

### Test Types

1. **Functional Tests**
   - `test_home_ui_loads`: Verifies the UI homepage returns HTTP 200
   - `test_negative_inputs`: Tests error handling (empty and oversized titles)

2. **Property-Based Tests**
   - `test_create_list_roundtrip`: Uses Hypothesis to generate 100+ test cases with valid titles and descriptions

3. **Contract Tests**
   - `test_contract_smoke`: Verifies `normalize_title` function obeys its contracts

4. **UI/E2E Tests**
   - `test_add_todo_and_screenshot`: Automates browser to add a todo and capture screenshot

5. **Formal Verification**
   - CrossHair symbolically executes `domain_contracts.py` to prove correctness

---

## Viewing Results

### 1. Coverage HTML Report

Open in browser:

```bash
# Windows
start htmlcov/index.html

# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html
```

**What You'll See:**
- Overall coverage percentage
- Per-file coverage breakdown
- Line-by-line highlighting (green = covered, red = missed)

### 2. UI Screenshot

View the captured screenshot:

```bash
# Windows
start artifacts/ui_after_add.png

# macOS
open artifacts/ui_after_add.png

# Linux
xdg-open artifacts/ui_after_add.png
```

### 3. Coverage XML

For CI/CD integration (e.g., Azure DevOps, Jenkins):

```bash
# Cobertura format
cat artifacts/coverage.xml
```

### 4. JUnit XML

For test result dashboards:

```bash
# JUnit format
cat artifacts/junit.xml
```

---

## Makefile Commands

The project includes a `Makefile` for convenience:

```bash
make run     # Start Flask server
make test    # Run pytest with quick output
make cov     # Generate all coverage reports (terminal + XML + HTML)
make ui      # Run UI tests only
make formal  # Run CrossHair formal verification
make all     # Run test + cov + junit + formal
make clean   # Remove artifacts and cache directories
```

**Usage:**

```bash
# Start server in Terminal A
make run

# Run everything in Terminal B
make all
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'imp'`

**Cause:** Old version of Flasgger doesn't support Python 3.12

**Fix:** Already resolved by upgrading to Flasgger 0.9.7.1

```bash
pip install --upgrade flasgger
```

---

### Issue: Pytest hangs at "collecting..."

**Cause:** `app.py` runs `app.run()` on import, blocking test collection

**Fix:** Already resolved by wrapping `app.run()` in `if __name__ == "__main__":`

---

### Issue: UI test fails with "Element not found"

**Cause:** HTML selectors in test don't match actual page elements

**Fix:** Use Playwright's codegen to discover correct selectors:

```bash
python -m playwright codegen http://127.0.0.1:5000
```

Copy the generated selectors and update `tests/test_ui_playwright.py`.

---

### Issue: Coverage report shows 0%

**Cause:** Ran `pytest` instead of `coverage run -m pytest`

**Fix:**

```bash
coverage run -m pytest
coverage report
```

---

### Issue: CrossHair reports timeout or "unknown"

**Cause:** Function is too complex or contracts are ambiguous

**Fix:**
- Simplify contracts
- Increase timeout: `crosshair check --per_condition_timeout=10 domain_contracts.py`

---

### Issue: Flask server won't start (port 5000 in use)

**Cause:** Another process is using port 5000

**Fix:**

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

Or change the port in `app.py`:

```python
app.run(debug=True, port=5001)
```

---

## Project Structure

```
flask-todo-app/
├── app.py                      # Flask application (modified for testing)
├── domain_contracts.py         # Business logic contracts (NEW)
├── conftest.py                 # Pytest configuration (NEW)
├── Makefile                    # Convenience commands (NEW)
├── requirements.txt            # Original app dependencies
├── REPORT.md                   # V&V report (NEW)
├── slides/SLIDES.md                   # Presentation outline (NEW)
├── VV_README.md                # This file (NEW)
├── tests/                      # Test suite (NEW)
│   ├── test_api_properties.py  # Functional + property tests
│   ├── test_contracts.py       # Contract tests
│   └── test_ui_playwright.py   # UI/E2E tests
├── artifacts/                  # Test outputs (NEW)
│   ├── coverage.xml            # Cobertura coverage report
│   ├── junit.xml               # JUnit test results
│   └── ui_after_add.png        # UI screenshot
├── htmlcov/                    # HTML coverage report (NEW)
│   └── index.html              # Open this in browser
├── .venv/                      # Virtual environment
├── templates/                  # Flask HTML templates (original)
└── todo.db                     # SQLite database (created on first run)
```

---

## Deliverables

### Submission Checklist

When submitting your V&V project, ensure you include:

- [ ] **Source Code**
  - [ ] `tests/` directory with all test files
  - [ ] `domain_contracts.py`
  - [ ] `conftest.py`
  - [ ] `Makefile`

- [ ] **Artifacts**
  - [ ] `artifacts/coverage.xml`
  - [ ] `artifacts/junit.xml`
  - [ ] `artifacts/ui_after_add.png`
  - [ ] `htmlcov/` directory (or screenshot of `index.html`)

- [ ] **Documentation**
  - [ ] `REPORT.md` (or PDF export)
  - [ ] `slides/SLIDES.md` (or PowerPoint/PDF export)
  - [ ] `VV_README.md` (this file)

- [ ] **Instructions**
  - [ ] Clear commands to reproduce all results
  - [ ] List of dependencies and versions

### Generating PDF Reports

**From Markdown (REPORT.md and slides/SLIDES.md):**

```bash
# Option 1: Pandoc
pandoc REPORT.md -o REPORT.pdf
pandoc slides/SLIDES.md -o slides/SLIDES.pdf -t beamer

# Option 2: VS Code Markdown PDF extension
# Install "Markdown PDF" extension
# Right-click file → Markdown PDF: Export (pdf)

# Option 3: Copy to Google Docs and export as PDF
```

---

## Next Steps After Running Tests

1. **Review Results**
   - Open `htmlcov/index.html` to see line-by-line coverage
   - Open `artifacts/ui_after_add.png` to verify UI test
   - Read pytest output to understand the failed test (INC-001)

2. **Fix the Bug (Optional for Project)**
   - Add title length validation in [app.py:152](app.py#L152)
   - Re-run tests to verify fix

3. **Expand Test Suite (Optional for Extra Credit)**
   - Add tests for uncovered endpoints (GET by ID, PUT, DELETE)
   - Add UI tests for edit and delete workflows
   - Increase coverage to 80%+

4. **Complete Report**
   - Fill in placeholders in `REPORT.md` (team names, dates)
   - Add screenshot of `htmlcov/index.html` to report
   - Export to PDF

5. **Prepare Presentation**
   - Use `slides/SLIDES.md` as outline
   - Add visuals (screenshots, diagrams)
   - Practice delivery (5 minutes per person)

6. **Submit**
   - Package all files (code, artifacts, report, slides)
   - Submit via Microsoft Teams by deadline

---

## Additional Resources

### Documentation

- **pytest:** https://docs.pytest.org/
- **Hypothesis:** https://hypothesis.readthedocs.io/
- **coverage.py:** https://coverage.readthedocs.io/
- **Playwright:** https://playwright.dev/python/
- **icontract:** https://icontract.readthedocs.io/
- **CrossHair:** https://crosshair.readthedocs.io/

### Original Application

- **Repository:** https://github.com/onurtacc/flask-todo-app
- **Swagger UI:** http://127.0.0.1:5000/apidocs (when app is running)

### V&V Resources

- **Property-Based Testing:** https://hypothesis.works/articles/what-is-property-based-testing/
- **Design by Contract:** https://en.wikipedia.org/wiki/Design_by_contract
- **Formal Methods:** https://www.hillelwayne.com/post/crosshair/

---

## Support

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) section
2. Review tool documentation (links above)
3. Verify Python version: `python --version` (should be 3.12+)
4. Ensure virtual environment is activated (prompt shows `.venv`)
5. Confirm Flask server is running (visit http://127.0.0.1:5000)

---

## License

This V&V test suite is provided for educational purposes as part of the SEN4013 Software Verification & Validation course project.

Original Flask Todo App: See https://github.com/onurtacc/flask-todo-app for license.

---

**Last Updated:** October 30, 2025
**Version:** 1.0
**Authors:** [Your Team Names]

