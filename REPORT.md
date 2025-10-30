# SEN4013 Software Verification & Validation — Flask Todo App

**Team:** [Your Names Here]
**Date:** January 16, 2026

---

## 1. Introduction

This report documents the Verification & Validation (V&V) activities performed on a Flask-based Todo application. The primary goal of V&V is to build confidence that the application meets its specifications (verification) and user needs (validation) through automated, repeatable testing and analysis.

**V&V Objectives:**
- Verify functional correctness of REST API endpoints
- Validate UI functionality through end-to-end testing
- Measure structural code coverage
- Apply property-based testing for edge cases
- Enforce runtime contracts for business rules
- Use solver-aided verification for formal guarantees

---

## 2. System Under Test (SUT)

**Application:** Flask Todo App
**Repository:** https://github.com/onurtacc/flask-todo-app
**Description:** A simple web-based todo list application with:
- **Web UI** for managing tasks (add, edit, complete, delete)
- **REST API** (`/api/todos`) for programmatic access
- **Swagger UI** at `/apidocs` for API documentation
- **SQLite Database** for persistence

**Technology Stack:**
- Flask 1.1.1 (web framework)
- Flask-SQLAlchemy 2.4.1 (ORM)
- Flasgger 0.9.7.1 (Swagger/OpenAPI integration)
- SQLite (database)

---

## 3. V&V Approach & Tools

### 3.1 Toolchain Overview

| Tool | Purpose | Citation |
|------|---------|----------|
| **pytest** | Unit and functional test framework with simple assertions and automatic test discovery | [docs.pytest.org](https://docs.pytest.org/) |
| **Hypothesis** | Property-based testing that automatically generates edge-case inputs based on specification patterns | [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/) |
| **coverage.py** | Structural code coverage measurement (statement, branch); outputs terminal, XML, and HTML reports | [coverage.readthedocs.io](https://coverage.readthedocs.io/) |
| **Playwright** | Browser automation for UI/E2E testing with screenshot capture across Chromium, Firefox, and WebKit | [playwright.dev](https://playwright.dev/python/) |
| **icontract** | Runtime design-by-contract with preconditions (`@require`) and postconditions (`@ensure`) that fail fast on violations | [icontract.readthedocs.io](https://icontract.readthedocs.io/) |
| **CrossHair** | Solver-backed formal verification that searches for contract counterexamples using symbolic execution and SMT solving | [crosshair.readthedocs.io](https://crosshair.readthedocs.io/) |

### 3.2 Test Strategy

1. **Functional Testing:** Test typical user workflows (CRUD operations) via API endpoints
2. **Property-Based Testing:** Use Hypothesis to generate hundreds of valid inputs matching regex patterns
3. **Negative Testing:** Verify proper error handling for invalid inputs
4. **UI/E2E Testing:** Automate browser interactions and capture visual evidence
5. **Structural Coverage:** Measure which code paths are exercised by tests
6. **Contract Verification:** Enforce business rules at runtime and verify with formal methods
7. **Regression Prevention:** All tests automated and repeatable in CI/CD pipelines

---

## 4. Test Cases & Results

### 4.1 Test Summary

| ID | Test Area | Type | Status | Notes |
|----|-----------|------|--------|-------|
| T01 | Home UI Load | Functional | ✅ PASS | UI returns HTTP 200 |
| T02 | Create/List Roundtrip | Property-Based | ✅ PASS | Hypothesis generated 100+ test cases |
| T03 | Empty Title Rejection | Negative | ✅ PASS | API correctly returns 400 |
| T04 | Excessive Title Length | Negative | ❌ FAIL | **INCIDENT:** App accepts 200-char titles without validation |
| T05 | Contract Normalization | Contract | ✅ PASS | Title normalization strips whitespace correctly |
| T06 | CrossHair Verification | Formal | ✅ PASS | No counterexamples found for contract invariants |
| T07 | UI Add Todo + Screenshot | E2E | ✅ PASS | Successfully added "Buy milk" via browser |

**Overall Results:** 6 passed, 1 failed (83% pass rate)

### 4.2 Detailed Test Cases

#### T01: Home UI Load
- **Input:** GET request to `/`
- **Expected:** HTTP 200, HTML page rendered
- **Actual:** HTTP 200
- **Status:** ✅ PASS

#### T02: Create/List Roundtrip (Property-Based)
- **Input:** Hypothesis-generated titles (1-40 chars, alphanumeric + punctuation) and descriptions (0-120 chars)
- **Expected:** POST `/api/todos` returns 200/201, subsequent GET includes the created item
- **Actual:** All 100+ generated test cases passed
- **Status:** ✅ PASS
- **Coverage:** Tests many edge cases like single-character titles, max-length titles, special characters

#### T03: Empty Title Rejection
- **Input:** POST `/api/todos` with `{"title": ""}`
- **Expected:** HTTP 400 or 422
- **Actual:** HTTP 400
- **Status:** ✅ PASS

#### T04: Excessive Title Length
- **Input:** POST `/api/todos` with `{"title": "x" * 200}` (200 characters)
- **Expected:** HTTP 400 or 422
- **Actual:** HTTP 201 (created successfully)
- **Status:** ❌ FAIL
- **Incident:** See Section 6

#### T05: Title Normalization Contract
- **Input:** `normalize_title("  Hello  ")`
- **Expected:** Returns `"Hello"` (trimmed), no contract violations
- **Actual:** `"Hello"`
- **Status:** ✅ PASS

#### T06: CrossHair Formal Verification
- **Command:** `crosshair check domain_contracts.py`
- **Expected:** No counterexamples found
- **Actual:** No output (success)
- **Status:** ✅ PASS
- **Note:** CrossHair verified that `normalize_title` cannot violate its contracts for any valid input

#### T07: UI Add Todo via Browser
- **Input:** Navigate to http://127.0.0.1:5000, fill form with "Buy milk" / "2L semi-skimmed", click Add
- **Expected:** Todo appears in list, screenshot captured
- **Actual:** Todo visible in page content, screenshot saved to `artifacts/ui_after_add.png`
- **Status:** ✅ PASS
- **Evidence:** See screenshot below

![UI Screenshot](artifacts/ui_after_add.png)

---

## 5. Structural Coverage

### 5.1 Coverage Summary

```
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
app.py                            95     45    53%   [see below]
conftest.py                        4      0   100%
domain_contracts.py                6      0   100%
tests\test_api_properties.py      28      0   100%
tests\test_contracts.py            3      0   100%
------------------------------------------------------------
TOTAL                            136     45    67%
```

**Overall Coverage:** 67%
**App Coverage:** 53%
**Test Code Coverage:** 100%

### 5.2 Uncovered Lines in app.py

The following lines were not exercised by the current test suite:

- **Lines 24-29:** Web form submission handler (`/add` POST)
- **Lines 33-36:** Complete todo via web UI (`/complete/<id>`)
- **Lines 40-43:** Incomplete todo via web UI (`/incomplete/<id>`)
- **Lines 47-50:** Delete todo via web UI (`/delete/<id>`)
- **Lines 54-59:** Edit todo via web UI (`/edit/<id>` POST)
- **Lines 115-116:** API get single todo by ID (`/api/todos/<id>` GET)
- **Line 150:** JSON validation error path in POST endpoint
- **Lines 202-214:** API update todo (`/api/todos/<id>` PUT)
- **Lines 239-242:** API delete todo (`/api/todos/<id>` DELETE)

**Analysis:**
- Current tests focus on the API create/list endpoints and basic UI load
- Web form handlers and remaining API endpoints (GET by ID, PUT, DELETE) are untested
- This represents gaps in test coverage that could hide defects

### 5.3 Coverage HTML Report

For detailed line-by-line coverage visualization, open: `htmlcov/index.html`

**Screenshot of Coverage Report:**

[PLACEHOLDER: Insert screenshot of htmlcov/index.html showing the coverage dashboard]

---

## 6. Incidents & Findings

### 6.1 Resolved Incidents

*None in this iteration*

### 6.2 Unresolved Incidents

#### INC-001: Missing Title Length Validation

**Severity:** Medium
**Status:** Open
**Test Case:** T04 - Excessive Title Length

**Description:**
The API endpoint `POST /api/todos` accepts arbitrarily long titles without validation. The database schema defines `title = db.Column(db.String(100), nullable=False)`, which suggests an intended 100-character limit, but the application code does not enforce this before attempting to store the data.

**Reproduction:**
```bash
curl -X POST http://127.0.0.1:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"'"$(python -c "print('x'*200)")"'"}'
# Returns HTTP 201 Created
```

**Expected Behavior:**
Should return HTTP 400 with error message: `{"error": "Title must be 100 characters or less"}`

**Actual Behavior:**
Returns HTTP 201, title is truncated by database (silent data loss) or causes unexpected behavior

**Impact:**
- **Data Integrity:** Potential silent truncation or database errors
- **User Experience:** No feedback when title is too long
- **Security:** Could be exploited for buffer overflow-style attacks if database layer doesn't truncate properly

**Recommendation:**
Add validation in `api_create_todo()` function ([app.py:152](app.py#L152)):

```python
if len(title) > 100:
    return jsonify({"error": "Title must be 100 characters or less"}), 400
```

**Risk if Unresolved:**
Low to Medium. SQLite will truncate to 100 chars, but users will experience unexpected behavior. Could escalate if migrated to a database that throws errors on oversized strings.

---

## 7. Limitations & Threats to Validity

### 7.1 Test Coverage Limitations

1. **Code Coverage ≠ Test Quality:** 67% structural coverage doesn't guarantee all logical paths or edge cases are tested
2. **UI Testing Scope:** Only one UI workflow (add todo) is tested; edit, delete, and complete actions via UI are untested
3. **Property Test Scope:** Hypothesis tests use regex patterns that may not cover all real-world inputs (e.g., Unicode, emoji, SQL injection)
4. **Contract Scope:** Contracts only cover `normalize_title` function; business rules in other parts of the app are not formally specified

### 7.2 Environmental Factors

1. **Single Browser:** Playwright tests only run in Chromium; Firefox and WebKit not tested
2. **SQLite Behavior:** Database truncation behavior may differ in production databases (PostgreSQL, MySQL)
3. **No Load/Stress Testing:** Performance and concurrency issues not covered

### 7.3 Oracle Problem

- Empty title rejection and length validation expectations are derived from typical web app behavior, not formal specifications
- No formal requirements document to validate against

---

## 8. Recommendations

### 8.1 Immediate Actions

1. **Fix INC-001:** Add title length validation (< 5 minutes)
2. **Expand Coverage:** Write tests for uncovered endpoints (GET by ID, PUT, DELETE) to reach 80%+ coverage
3. **Property Test Enhancement:** Add Hypothesis strategies for Unicode, emoji, and SQL injection patterns

### 8.2 Process Improvements

1. **Continuous Integration:** Run `pytest`, `coverage`, and `crosshair` on every commit via GitHub Actions
   ```yaml
   - run: pytest --cov --junitxml=junit.xml
   - run: coverage xml
   - run: crosshair check domain_contracts.py
   ```

2. **Contract-Driven Development:** Add icontract pre/postconditions to all API endpoints:
   - `@require(lambda title: 1 <= len(title) <= 100)`
   - `@ensure(lambda result: result[1] in {200, 201, 400, 404})`

3. **Extended Property Testing:** Use Hypothesis for:
   - Stateful testing (sequences of API calls)
   - Database roundtrip properties (write then read should match)
   - Idempotency checks (PUT same data twice = same result)

4. **Formal Specification:** Document API contracts in OpenAPI/Swagger with JSON Schema validation, then auto-generate tests

### 8.3 Long-Term Strategy

1. **Mutation Testing:** Use `mutmut` to verify tests catch injected bugs
2. **Fuzzing:** Apply `atheris` to find crash-inducing inputs
3. **Model Checking:** For complex workflows, use TLA+ or Alloy to verify state machine properties

---

## 9. Conclusion

This V&V effort successfully applied multiple testing techniques to the Flask Todo application, achieving 67% code coverage and identifying one medium-severity input validation defect (INC-001). The combination of functional, property-based, contract, and formal verification methods demonstrates a comprehensive approach to building confidence in software quality.

**Key Achievements:**
- Automated test suite with 6/7 tests passing (83% pass rate)
- Property-based testing with 100+ auto-generated test cases
- Formal verification confirming contract invariants
- Visual evidence via browser automation screenshot
- Detailed coverage analysis identifying untested code paths

**Next Steps:**
1. Resolve INC-001 (title length validation)
2. Increase coverage to 80%+ by testing remaining endpoints
3. Integrate tests into CI/CD pipeline
4. Expand contracts to cover more business logic

The artifacts produced (coverage reports, test results, screenshots) provide auditable evidence of quality for stakeholders and support continuous improvement of the V&V process.

---

## 10. Appendix A: Tool Installation & Usage

### pytest
- **Installation:** `pip install pytest`
- **Usage:** `pytest -v`
- **Documentation:** https://docs.pytest.org/

### Hypothesis
- **Installation:** `pip install hypothesis`
- **Usage:** Decorate test functions with `@given(st.text())`
- **Documentation:** https://hypothesis.readthedocs.io/

### coverage.py
- **Installation:** `pip install coverage`
- **Usage:**
  ```bash
  coverage run -m pytest
  coverage report -m
  coverage html  # open htmlcov/index.html
  ```
- **Documentation:** https://coverage.readthedocs.io/

### Playwright
- **Installation:**
  ```bash
  pip install playwright pytest-playwright
  python -m playwright install
  ```
- **Usage:** `pytest -v tests/test_ui_playwright.py`
- **Code Generation:** `python -m playwright codegen http://127.0.0.1:5000`
- **Documentation:** https://playwright.dev/python/

### icontract
- **Installation:** `pip install icontract`
- **Usage:**
  ```python
  from icontract import require, ensure

  @require(lambda x: x > 0)
  @ensure(lambda result: result >= 0)
  def sqrt(x):
      return x ** 0.5
  ```
- **Documentation:** https://icontract.readthedocs.io/

### CrossHair
- **Installation:** `pip install crosshair-tool`
- **Usage:** `crosshair check domain_contracts.py`
- **Documentation:** https://crosshair.readthedocs.io/

---

## 11. Appendix B: Running the Tests

### Prerequisites
```bash
# Clone the repository
git clone https://github.com/onurtacc/flask-todo-app
cd flask-todo-app

# Create virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install pytest hypothesis coverage icontract crosshair-tool playwright pytest-playwright
python -m playwright install
```

### Running All Tests
```bash
# Start the Flask app in Terminal A
python app.py

# In Terminal B, run tests
make all  # or run commands below individually

# Individual commands:
pytest -v                              # Run all tests
coverage run -m pytest                 # Collect coverage
coverage report -m                     # View coverage summary
coverage html                          # Generate HTML report
pytest --junitxml=artifacts/junit.xml  # Generate JUnit XML
crosshair check domain_contracts.py    # Formal verification
```

### Makefile Targets
```bash
make run     # Start Flask server
make test    # Run pytest
make cov     # Generate coverage reports
make ui      # Run UI tests
make formal  # Run CrossHair
make all     # Run all tests and coverage
```

---

## 12. Appendix C: Artifacts

All test artifacts are stored in the `artifacts/` directory:

1. **coverage.xml** - Cobertura XML format for CI/CD integration
2. **junit.xml** - JUnit XML test results for CI/CD dashboards
3. **ui_after_add.png** - Screenshot of UI after adding a todo item
4. **htmlcov/** - HTML coverage report (open `htmlcov/index.html`)

---

**Report prepared by:** [Your Names]
**Last updated:** [Date]
**Version:** 1.0
