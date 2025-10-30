# V&V Project Submission Guide
## Step-by-Step Instructions for Completing Your Project

This guide walks you through every step from running tests to submitting your final deliverables.

---

## Table of Contents

1. [Getting All Screenshots](#1-getting-all-screenshots)
2. [Verifying Your Test Results](#2-verifying-your-test-results)
3. [Completing the Report](#3-completing-the-report)
4. [Creating the Presentation](#4-creating-the-presentation)
5. [Exporting to PDF](#5-exporting-to-pdf)
6. [Organizing Deliverables](#6-organizing-deliverables)
7. [Final Checklist](#7-final-checklist)
8. [Submission Instructions](#8-submission-instructions)

---

## 1. Getting All Screenshots

You need several screenshots for your report and presentation. Here's how to get each one.

### Screenshot 1: Coverage HTML Report ⭐ REQUIRED

**Purpose:** Shows line-by-line code coverage with green/red highlighting

**Steps:**

1. **Open the coverage report in your browser:**

   ```bash
   # Windows
   cd flask-todo-app
   start htmlcov\index.html

   # macOS
   open htmlcov/index.html

   # Linux
   xdg-open htmlcov/index.html
   ```

2. **Your browser will show the coverage dashboard:**
   - Total coverage percentage (67%)
   - List of files with individual coverage
   - Module listing

3. **Take a screenshot of the main dashboard:**
   - **Windows:** Press `Win + Shift + S`, select area, save to `screenshots/coverage_dashboard.png`
   - **macOS:** Press `Cmd + Shift + 4`, drag to select, saves to Desktop
   - **Full window:** Use your browser's screenshot tool (F12 → ... → Screenshot)

4. **Optional: Take a screenshot of app.py detail:**
   - Click on "app.py" in the coverage report
   - You'll see the source code with green (covered) and red (missed) lines
   - Screenshot this view showing the uncovered lines
   - Save as `screenshots/coverage_app_detail.png`

**What to include in report:**
- Coverage dashboard showing 67% total coverage
- Optional: Detail view showing which lines are uncovered

---

### Screenshot 2: UI After Adding Todo ✅ ALREADY CAPTURED

**Purpose:** Visual proof that the UI test worked

**Location:** `flask-todo-app/artifacts/ui_after_add.png`

**Steps:**

1. **View the screenshot:**

   ```bash
   # Windows
   start artifacts\ui_after_add.png

   # macOS
   open artifacts/ui_after_add.png

   # Linux
   xdg-open artifacts/ui_after_add.png
   ```

2. **Verify it shows:**
   - The Flask todo app UI
   - "Buy milk" todo item visible
   - Full page screenshot

3. **If screenshot is missing or you want a new one:**

   ```bash
   # Ensure Flask is running
   python app.py  # in Terminal 1

   # Run UI test
   pytest tests/test_ui_playwright.py -v  # in Terminal 2

   # Screenshot will be saved to artifacts/ui_after_add.png
   ```

**What to include in report:**
- This screenshot in Section 4.2 (Test T07) or Section 11 (UI E2E Testing slide)

---

### Screenshot 3: Swagger API Documentation (Optional but Impressive)

**Purpose:** Shows the auto-generated API documentation

**Steps:**

1. **Ensure Flask is running:**

   ```bash
   python app.py
   ```

2. **Open Swagger UI:**

   Navigate to: http://127.0.0.1:5000/apidocs/

3. **You'll see the Swagger interface with:**
   - List of all API endpoints
   - Interactive "Try it out" buttons
   - Request/response schemas

4. **Take a screenshot:**
   - Expand one endpoint (e.g., "POST /api/todos")
   - Show the request schema
   - Save as `screenshots/swagger_ui.png`

**What to include in report:**
- Section 2 (System Under Test) to show API documentation
- Demonstrates the app has well-documented interfaces

---

### Screenshot 4: Pytest Output (Terminal)

**Purpose:** Shows test execution and results

**Steps:**

1. **Run pytest with verbose output:**

   ```bash
   pytest -v
   ```

2. **You'll see output like:**

   ```
   ============================= test session starts =============================
   tests/test_api_properties.py::test_home_ui_loads PASSED          [ 20%]
   tests/test_api_properties.py::test_create_list_roundtrip PASSED  [ 40%]
   tests/test_api_properties.py::test_negative_inputs FAILED        [ 60%]
   tests/test_contracts.py::test_contract_smoke PASSED              [ 80%]
   tests/test_ui_playwright.py::test_add_todo_and_screenshot PASSED [100%]

   ==================== 1 failed, 4 passed in XX.XXs ==========================
   ```

3. **Take a screenshot of your terminal:**
   - **Windows:** Windows Terminal → Right-click → Export as → SVG/PNG, or use Snipping Tool
   - **macOS:** Cmd + Shift + 4 → Select terminal window
   - Save as `screenshots/pytest_output.png`

**What to include in report:**
- Section 4.1 (Test Summary) to show actual test execution
- Shows the expected failure (INC-001)

---

### Screenshot 5: Coverage Terminal Report

**Purpose:** Shows coverage percentages in terminal

**Steps:**

1. **Generate coverage report:**

   ```bash
   coverage run -m pytest
   coverage report -m
   ```

2. **You'll see output like:**

   ```
   Name                           Stmts   Miss  Cover   Missing
   ------------------------------------------------------------
   app.py                            95     45    53%   24-29, 33-36, ...
   conftest.py                        4      0   100%
   domain_contracts.py                6      0   100%
   tests\test_api_properties.py      28      0   100%
   tests\test_contracts.py            3      0   100%
   ------------------------------------------------------------
   TOTAL                            136     45    67%
   ```

3. **Screenshot this terminal output:**
   - Save as `screenshots/coverage_terminal.png`

**What to include in report:**
- Section 5.1 (Coverage Summary) - you can paste this as a code block or image

---

### Screenshot 6: Flask App Running

**Purpose:** Shows the actual application UI

**Steps:**

1. **Start Flask:**

   ```bash
   python app.py
   ```

2. **Open in browser:**

   Navigate to: http://127.0.0.1:5000

3. **Take screenshots of:**
   - Homepage with empty todo list
   - Homepage after adding a few todos
   - Save as `screenshots/app_ui_home.png`

**What to include in report:**
- Section 2 (System Under Test) to show what the app looks like
- Slide 3 of presentation (System Under Test)

---

### Organizing Your Screenshots

Create a `screenshots/` folder and organize:

```bash
cd flask-todo-app
mkdir screenshots

# Move/copy your screenshots here:
screenshots/
├── coverage_dashboard.png       ⭐ REQUIRED
├── coverage_app_detail.png      (optional)
├── pytest_output.png            ⭐ REQUIRED
├── coverage_terminal.png        (optional - can use text instead)
├── swagger_ui.png               (optional but impressive)
└── app_ui_home.png              (optional)

# Already captured:
artifacts/
└── ui_after_add.png             ⭐ REQUIRED
```

---

## 2. Verifying Your Test Results

Before completing your report, verify everything ran successfully.

### Check 1: Test Execution

```bash
pytest -v
```

**Expected Results:**
- ✅ 4 tests passed
- ❌ 1 test failed (test_negative_inputs) — THIS IS EXPECTED
- Total: 5 tests collected

**What the failure means:**
- This is **INC-001** - the bug you discovered
- The app incorrectly accepts 200-character titles
- This is a **feature, not a bug in your tests**
- Document this as a finding!

---

### Check 2: Coverage Generated

```bash
# Check coverage files exist
ls artifacts/coverage.xml
ls htmlcov/index.html

# View coverage summary
coverage report
```

**Expected:**
- Coverage XML exists: `artifacts/coverage.xml`
- HTML report exists: `htmlcov/index.html`
- Total coverage: ~67%

---

### Check 3: UI Screenshot Captured

```bash
# Check screenshot exists
ls -lh artifacts/ui_after_add.png

# Should show file size around 900KB - 1MB
```

**If missing:**

```bash
# Run UI test again
pytest tests/test_ui_playwright.py -v
```

---

### Check 4: JUnit XML Generated

```bash
ls artifacts/junit.xml
```

**If missing:**

```bash
pytest --junitxml=artifacts/junit.xml
```

---

### Check 5: CrossHair Verification

```bash
crosshair check domain_contracts.py
```

**Expected:**
- No output (success)
- Exit code 0

**If you see errors:**
- Read the error message
- CrossHair may report timeout or counterexamples
- Document this as a finding in your report

---

## 3. Completing the Report

Your report template is in `REPORT.md`. Here's what to fill in:

### Step 1: Update Team Information

**Find and replace:**
- `[Your Names Here]` → Your team member names
- `[Your Names]` → Your team member names (appears multiple times)
- `January 16, 2026` → Actual submission date
- `[Date]` → Current date

**Use Find & Replace:**

```bash
# Open REPORT.md in VS Code or text editor
# Find: [Your Names Here]
# Replace with: John Doe, Jane Smith, Alice Johnson, Bob Lee

# Find: January 16, 2026
# Replace with: October 30, 2025
```

---

### Step 2: Insert Screenshots

**Section 4.2 (Test T07):**

Replace:
```markdown
![UI Screenshot](artifacts/ui_after_add.png)
```

With actual screenshot reference or embed the image.

**Section 5.3 (Coverage HTML Report):**

Replace:
```markdown
[PLACEHOLDER: Insert screenshot of htmlcov/index.html showing the coverage dashboard]
```

With:
```markdown
![Coverage Dashboard](screenshots/coverage_dashboard.png)

**Key Findings:**
- 67% overall coverage achieved
- API endpoints well-covered (create, list, error handling)
- Gaps in web form handlers and remaining API endpoints (GET by ID, PUT, DELETE)
```

---

### Step 3: Review Test Results

**Section 4.1 (Test Summary):**

Verify the table matches your actual results:
- 6 passed, 1 failed ✅ (this should match your pytest output)
- 83% pass rate ✅

**If your results differ:**
- Update the table with actual results
- Update the pass rate calculation

---

### Step 4: Verify Coverage Numbers

**Section 5.1:**

Check that the coverage table matches your `coverage report` output:

```bash
coverage report -m
```

Copy the exact output and paste it into the report.

---

### Step 5: Review Incident INC-001

**Section 6.2:**

Verify the incident description matches what you observed:

1. **Confirm the bug:**

   ```bash
   # In Terminal 2 (with Flask running in Terminal 1):
   curl -X POST http://127.0.0.1:5000/api/todos \
     -H "Content-Type: application/json" \
     -d "{\"title\":\"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"}"
   ```

   (That's 200 x's)

   **Expected:** Returns HTTP 201 (bug confirmed)

2. **Document in report:**
   - You've already documented this in Section 6.2
   - Just verify the reproduction steps work

---

### Step 6: Add Your Analysis (Optional Enhancement)

**Section 7 (Limitations):**

Add any limitations you observed during testing, for example:

```markdown
### 7.2 Environmental Factors (UPDATED)

1. **Single Browser:** Playwright tests only run in Chromium; Firefox and WebKit not tested
2. **SQLite Behavior:** Database truncation behavior may differ in production databases
3. **No Load/Stress Testing:** Performance and concurrency issues not covered
4. **Windows-Only Testing:** Tests run on Windows; behavior on macOS/Linux not verified
5. **No Security Testing:** SQL injection, XSS, CSRF not tested
```

---

### Step 7: Save and Review

1. Save `REPORT.md`
2. Read through the entire document
3. Check for any remaining `[PLACEHOLDER]` text
4. Verify all links work (e.g., `[app.py:152](app.py#L152)`)
5. Spell-check and grammar-check

---

## 4. Creating the Presentation

Your presentation outline is in `SLIDES.md`. Here's how to turn it into slides:

### Option 1: Use Markdown to Slides Tools

#### A. Marp (Recommended - Makes Beautiful Slides)

1. **Install Marp CLI:**

   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Convert to PDF:**

   ```bash
   cd flask-todo-app
   marp SLIDES.md -o SLIDES.pdf
   ```

3. **Or create PowerPoint:**

   ```bash
   marp SLIDES.md -o SLIDES.pptx
   ```

4. **Preview in VS Code:**
   - Install "Marp for VS Code" extension
   - Open SLIDES.md
   - Click "Open Preview to the Side"

---

#### B. reveal.js (Web-Based Presentation)

1. **Install reveal-md:**

   ```bash
   npm install -g reveal-md
   ```

2. **Present live:**

   ```bash
   reveal-md SLIDES.md
   ```

   Opens in browser at http://localhost:1948

3. **Export to PDF:**

   ```bash
   reveal-md SLIDES.md --print SLIDES.pdf
   ```

---

#### C. Pandoc (Convert to Beamer PDF)

1. **Install Pandoc:** https://pandoc.org/installing.html

2. **Convert to PDF:**

   ```bash
   pandoc SLIDES.md -t beamer -o SLIDES.pdf
   ```

---

### Option 2: Manually Create PowerPoint/Google Slides

**Steps:**

1. **Open PowerPoint or Google Slides**

2. **Create slides from SLIDES.md:**

   - **Slide 1:** Copy title and team info
   - **Slide 2:** Copy "What is Verification & Validation?" content
   - **Slide 3:** Copy "System Under Test" content
   - ...continue for all 14 slides

3. **Add visuals:**
   - Slide 3: Insert screenshot from `screenshots/app_ui_home.png`
   - Slide 10: Insert `screenshots/coverage_dashboard.png`
   - Slide 11: Insert `artifacts/ui_after_add.png`
   - Slide 4: Add tool logos (search "pytest logo", "hypothesis logo", etc.)

4. **Add speaker notes:**
   - Copy the "Speaker Notes" sections from SLIDES.md
   - Paste into PowerPoint's notes pane (View → Notes)
   - Or Google Slides: Insert → Speaker notes

5. **Format for readability:**
   - Use 24pt+ font size
   - High contrast colors
   - Bullet points, not paragraphs
   - Maximum 7 lines per slide

6. **Export to PDF:**
   - PowerPoint: File → Export → PDF
   - Google Slides: File → Download → PDF

---

### Step-by-Step Slide Creation Example

**Slide 4: V&V Toolchain**

1. Create table with 3 columns: Tool | Purpose | Why We Used It
2. Add 6 rows for each tool
3. Optional: Add tool icons/logos to the left of each tool name
4. Add speaker notes at bottom
5. Use consistent formatting (color, fonts)

**Visuals to include:**

- Slide 3: App UI screenshot
- Slide 4: Tool logos (pytest, Hypothesis, coverage.py, Playwright, icontract, CrossHair)
- Slide 6: Code snippet showing `test_home_ui_loads`
- Slide 7: Code snippet showing `@given` decorator
- Slide 8: Code snippet showing `@require` and `@ensure`
- Slide 9: Diagram of symbolic execution (draw or find online)
- Slide 10: Coverage dashboard screenshot ⭐
- Slide 11: UI screenshot ⭐
- Slide 12: Red "bug" icon or warning symbol

---

## 5. Exporting to PDF

### Export REPORT.md to PDF

#### Option 1: Pandoc (Best Quality)

```bash
cd flask-todo-app

# Basic export
pandoc REPORT.md -o REPORT.pdf

# With table of contents
pandoc REPORT.md -o REPORT.pdf --toc --toc-depth=2

# With better formatting
pandoc REPORT.md -o REPORT.pdf \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --highlight-style=tango \
  -V geometry:margin=1in
```

---

#### Option 2: VS Code Extension

1. **Install "Markdown PDF" extension:**
   - Open VS Code
   - Extensions panel (Ctrl+Shift+X)
   - Search "Markdown PDF"
   - Install by yzane

2. **Convert:**
   - Open REPORT.md in VS Code
   - Right-click in the editor
   - Select "Markdown PDF: Export (pdf)"
   - PDF saved in same directory

3. **Configure options (optional):**
   - File → Preferences → Settings
   - Search "markdown-pdf"
   - Adjust margins, styles, etc.

---

#### Option 3: Google Docs

1. **Copy content:**
   - Open REPORT.md in VS Code or text editor
   - Select all (Ctrl+A), copy (Ctrl+C)

2. **Paste into Google Docs:**
   - Go to https://docs.google.com
   - Create new document
   - Paste (Ctrl+V)
   - Markdown will be converted to formatted text

3. **Fix formatting:**
   - Add headings (Format → Paragraph styles)
   - Insert images (Insert → Image → Upload from computer)
   - Add page breaks (Insert → Break → Page break)

4. **Export:**
   - File → Download → PDF Document (.pdf)

---

#### Option 4: Grip (GitHub-Style Preview)

```bash
# Install grip
pip install grip

# Preview in browser
cd flask-todo-app
grip REPORT.md

# Opens at http://localhost:6419
# Print to PDF using browser's print function (Ctrl+P → Save as PDF)
```

---

### Export SLIDES.md to PDF

See [Section 4 - Creating the Presentation](#4-creating-the-presentation) above.

**Quick options:**
- Marp: `marp SLIDES.md -o SLIDES.pdf`
- Pandoc: `pandoc SLIDES.md -t beamer -o SLIDES.pdf`
- Manual: Create in PowerPoint/Google Slides → Export to PDF

---

## 6. Organizing Deliverables

Create a clean folder structure for submission.

### Step 1: Create Submission Folder

```bash
cd "C:\Users\User\OneDrive\Downloads\Uni\Project - Software Validation\Tasks"

# Create submission folder
mkdir VV_Project_Submission
cd VV_Project_Submission
```

---

### Step 2: Copy Required Files

```bash
# Copy entire flask-todo-app directory
cp -r ../flask-todo-app ./

# Or copy selectively:
mkdir src tests artifacts docs screenshots

# Source code
cp ../flask-todo-app/app.py ./src/
cp ../flask-todo-app/domain_contracts.py ./src/
cp ../flask-todo-app/conftest.py ./src/
cp ../flask-todo-app/Makefile ./src/

# Tests
cp -r ../flask-todo-app/tests/* ./tests/

# Artifacts
cp -r ../flask-todo-app/artifacts/* ./artifacts/
cp -r ../flask-todo-app/htmlcov ./artifacts/

# Documentation
cp ../flask-todo-app/REPORT.md ./docs/
cp ../flask-todo-app/REPORT.pdf ./docs/
cp ../flask-todo-app/SLIDES.md ./docs/
cp ../flask-todo-app/SLIDES.pdf ./docs/
cp ../flask-todo-app/VV_README.md ./docs/

# Screenshots
cp ../flask-todo-app/screenshots/* ./screenshots/
```

---

### Step 3: Create Submission README

Create `VV_Project_Submission/README.md`:

```markdown
# SEN4013 V&V Project Submission

**Team Members:** [Your Names]
**Date:** [Submission Date]
**Project:** Verification & Validation of Flask Todo Application

## Contents

- `docs/` - Reports and presentation
  - `REPORT.pdf` - Full V&V report (12 sections)
  - `SLIDES.pdf` - Presentation slides (14 slides)
  - `VV_README.md` - Setup and run instructions

- `src/` - Source code
  - `app.py` - Flask application (modified for testing)
  - `domain_contracts.py` - Business logic contracts
  - `conftest.py` - Pytest configuration
  - `Makefile` - Convenience commands

- `tests/` - Test suite
  - `test_api_properties.py` - Functional + property-based tests
  - `test_contracts.py` - Contract tests
  - `test_ui_playwright.py` - UI/E2E tests

- `artifacts/` - Test results and evidence
  - `coverage.xml` - Cobertura coverage report
  - `junit.xml` - JUnit test results
  - `ui_after_add.png` - UI test screenshot
  - `htmlcov/` - HTML coverage report (open index.html)

- `screenshots/` - Additional evidence
  - `coverage_dashboard.png` - Coverage overview
  - `pytest_output.png` - Test execution
  - (other screenshots as captured)

## Running Tests

See `docs/VV_README.md` for complete instructions.

Quick start:
```bash
cd ../flask-todo-app  # (go back to original project)
.venv\Scripts\activate
python app.py  # Terminal 1
make all       # Terminal 2
```

## Summary

- **Tests:** 5 total (4 passed, 1 failed - expected)
- **Coverage:** 67%
- **Bugs Found:** 1 (INC-001: Missing title length validation)
- **Tools Used:** pytest, Hypothesis, coverage.py, Playwright, icontract, CrossHair

## Incident Report

**INC-001: Missing Title Length Validation**
- Severity: Medium
- Status: Documented in report
- Fix: Add length check at app.py:152

See `docs/REPORT.pdf` for full details.
```

---

### Step 4: Verify Folder Structure

```
VV_Project_Submission/
├── README.md                    ← Quick overview
├── docs/
│   ├── REPORT.pdf              ⭐ REQUIRED
│   ├── SLIDES.pdf              ⭐ REQUIRED
│   ├── REPORT.md               (optional - Markdown source)
│   ├── SLIDES.md               (optional - Markdown source)
│   └── VV_README.md            ⭐ REQUIRED
├── src/
│   ├── app.py
│   ├── domain_contracts.py
│   ├── conftest.py
│   └── Makefile
├── tests/
│   ├── test_api_properties.py  ⭐ REQUIRED
│   ├── test_contracts.py       ⭐ REQUIRED
│   └── test_ui_playwright.py   ⭐ REQUIRED
├── artifacts/
│   ├── coverage.xml            ⭐ REQUIRED
│   ├── junit.xml               ⭐ REQUIRED
│   ├── ui_after_add.png        ⭐ REQUIRED
│   └── htmlcov/
│       └── index.html          ⭐ REQUIRED
└── screenshots/
    ├── coverage_dashboard.png  ⭐ RECOMMENDED
    └── pytest_output.png       ⭐ RECOMMENDED
```

---

### Step 5: Create ZIP Archive

```bash
# Windows (PowerShell)
Compress-Archive -Path VV_Project_Submission -DestinationPath VV_Project_YourNames.zip

# Windows (Command Prompt with 7-Zip)
7z a VV_Project_YourNames.zip VV_Project_Submission

# macOS/Linux
zip -r VV_Project_YourNames.zip VV_Project_Submission
```

**Verify ZIP contents:**

```bash
# Windows
7z l VV_Project_YourNames.zip

# macOS/Linux
unzip -l VV_Project_YourNames.zip
```

---

## 7. Final Checklist

Before submitting, verify everything is complete:

### Documentation Checklist

- [ ] **REPORT.pdf exists and is complete**
  - [ ] All `[PLACEHOLDER]` text replaced
  - [ ] Team names filled in
  - [ ] Dates updated
  - [ ] Screenshots inserted
  - [ ] Coverage numbers match your results
  - [ ] INC-001 documented
  - [ ] All 12 sections complete
  - [ ] File size reasonable (< 20MB)

- [ ] **SLIDES.pdf exists and is complete**
  - [ ] All 14 slides included
  - [ ] Visuals added (screenshots, logos, diagrams)
  - [ ] Speaker notes included (if PowerPoint)
  - [ ] Team names on title slide
  - [ ] File size reasonable (< 10MB)

- [ ] **VV_README.md included**
  - [ ] Clear setup instructions
  - [ ] All commands tested and working

### Code Checklist

- [ ] **Test files exist and run:**
  - [ ] `tests/test_api_properties.py`
  - [ ] `tests/test_contracts.py`
  - [ ] `tests/test_ui_playwright.py`
  - [ ] All tests execute (even if 1 fails)

- [ ] **Source files included:**
  - [ ] `app.py` (modified with `if __name__ == "__main__"`)
  - [ ] `domain_contracts.py`
  - [ ] `conftest.py`
  - [ ] `Makefile`

### Artifacts Checklist

- [ ] **coverage.xml exists** (Cobertura format, ~5-10KB)
- [ ] **junit.xml exists** (JUnit format, ~2-5KB)
- [ ] **ui_after_add.png exists** (~900KB-1MB)
- [ ] **htmlcov/index.html exists** (can open and view in browser)

### Screenshots Checklist

- [ ] **coverage_dashboard.png** - Shows 67% coverage
- [ ] **pytest_output.png** - Shows 4 passed, 1 failed
- [ ] At least 2 screenshots total

### Quality Checks

- [ ] **Run tests one final time:**
  ```bash
  cd flask-todo-app
  .venv\Scripts\activate
  pytest -v  # Should show 4 passed, 1 failed
  ```

- [ ] **Verify coverage HTML opens:**
  ```bash
  start htmlcov\index.html  # Should open in browser
  ```

- [ ] **Check ZIP file size:** Should be < 50MB
  - If > 50MB, remove `.venv/` from submission
  - Include only source code, tests, artifacts, docs

- [ ] **Test ZIP extraction:**
  - Extract to a temporary folder
  - Verify all files are there
  - Try opening REPORT.pdf and SLIDES.pdf

---

## 8. Submission Instructions

### Step 1: Prepare for Upload

1. **Final filename check:**
   ```
   VV_Project_[YourTeamName].zip

   Examples:
   - VV_Project_TeamAlpha.zip
   - VV_Project_SmithJohnsonLeeWang.zip
   ```

2. **File size check:**
   ```bash
   # Windows
   dir VV_Project_*.zip

   # Should be < 50MB
   # If larger, exclude .venv/ and node_modules/
   ```

---

### Step 2: Submit via Microsoft Teams

**According to your project guide:**

1. **Open Microsoft Teams**

2. **Navigate to your course team:**
   - SEN4013 Software Verification & Validation

3. **Find the Assignments channel or Submission area**

4. **Upload your ZIP file:**
   - Click "Add attachment" or "Upload"
   - Select `VV_Project_YourTeamName.zip`
   - Wait for upload to complete

5. **Add a message with your submission:**

   ```
   Team: [Your Names]
   Date: [Submission Date]

   This submission includes:
   - Full V&V report (REPORT.pdf)
   - Presentation slides (SLIDES.pdf)
   - Test suite (pytest, Hypothesis, Playwright, icontract, CrossHair)
   - Test artifacts (coverage XML/HTML, JUnit XML, UI screenshot)
   - Setup instructions (VV_README.md)

   Summary:
   - 5 tests implemented (4 passed, 1 expected failure)
   - 67% code coverage achieved
   - 1 defect discovered (INC-001: Missing title length validation)
   - All deliverables complete

   Thank you!
   ```

6. **Submit and verify:**
   - Click "Submit" or "Send"
   - Check that your submission appears in the assignments list
   - Take a screenshot of the confirmation for your records

---

### Step 3: Alternative Submission (if Teams has issues)

**If Microsoft Teams doesn't work:**

1. **Email submission:**
   - Email to: [instructor email from syllabus]
   - Subject: SEN4013 V&V Project Submission - [Team Name]
   - Attach: `VV_Project_YourTeamName.zip`
   - Include: Same message as above

2. **Cloud storage link:**
   - Upload to OneDrive/Google Drive/Dropbox
   - Set permissions to "Anyone with link can view"
   - Share link via Teams or email
   - **Note:** Include download instructions if needed

---

## 9. Post-Submission

### After You Submit

1. **Keep a backup:**
   - Copy `VV_Project_YourTeamName.zip` to multiple locations
   - Save to cloud storage (OneDrive, Google Drive)
   - Keep local copy on USB drive

2. **Prepare for presentation:**
   - If in-class presentation required, practice with SLIDES.pdf
   - Allocate ~5 minutes per team member
   - Prepare for Q&A (review Section 13-14 of SLIDES.md "Backup Slides")

3. **Celebrate!** 🎉
   - You've completed a comprehensive V&V project
   - You discovered a real bug (INC-001)
   - You gained experience with 6 professional testing tools

---

## 10. Common Issues & Solutions

### Issue: PDF looks bad or has formatting issues

**Solution:**
- Use Pandoc with custom options (see Section 5)
- Or manually create in Google Docs/Word with better control
- Ensure images are embedded, not just linked

---

### Issue: ZIP file is too large (> 50MB)

**Solution:**
```bash
# Exclude virtual environment
zip -r VV_Project.zip VV_Project_Submission -x "*.venv/*" "*node_modules/*" "*.pyc" "*__pycache__/*"

# Or manually delete large folders before zipping:
rm -rf VV_Project_Submission/.venv
rm -rf VV_Project_Submission/node_modules
```

---

### Issue: Screenshots are missing from PDF

**Solution:**
- Use absolute paths when inserting images in Markdown
- Or embed images as base64 (increases file size)
- Or manually insert in Google Docs/Word before exporting

---

### Issue: Can't run tests after copying files

**Solution:**
```bash
# Reinstall dependencies in new location
cd VV_Project_Submission
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install pytest hypothesis coverage icontract crosshair-tool playwright pytest-playwright
python -m playwright install
```

---

### Issue: Instructor can't open/view artifacts

**Solution:**
- Include screenshots of artifacts IN the report PDF itself
- Add a "Viewing Artifacts" section in README
- Provide alternative formats (CSV for coverage, plain text for junit)

---

## 11. Extra Credit Opportunities (If Offered)

Want to go above and beyond? Here are optional enhancements:

### 1. Fix INC-001 and Re-Test

**Steps:**
1. Open `src/app.py`
2. Find line 152 (in `api_create_todo` function)
3. Add validation:
   ```python
   if len(title) > 100:
       return jsonify({"error": "Title must be 100 characters or less"}), 400
   ```
4. Re-run tests: `pytest -v`
5. Verify all 5 tests pass
6. Document fix in report appendix

---

### 2. Increase Coverage to 80%+

**Steps:**
1. Write tests for uncovered endpoints:
   - `test_api_get_todo_by_id()`
   - `test_api_update_todo()`
   - `test_api_delete_todo()`
2. Write tests for web form handlers:
   - `test_web_add_todo()`
   - `test_web_complete_todo()`
3. Re-run coverage: `coverage run -m pytest && coverage report`
4. Update report with new coverage numbers

---

### 3. Add Mutation Testing

**Steps:**
1. Install mutmut: `pip install mutmut`
2. Run mutation testing: `mutmut run`
3. Check results: `mutmut results`
4. Document in report: "We applied mutation testing to verify test quality. X% of mutations were caught."

---

### 4. Cross-Browser Testing

**Steps:**
1. Update `test_ui_playwright.py` to test Firefox and WebKit:
   ```python
   @pytest.mark.parametrize("browser_type", ["chromium", "firefox", "webkit"])
   def test_add_todo_cross_browser(browser_type):
       with sync_playwright() as p:
           browser = getattr(p, browser_type).launch()
           # ... rest of test
   ```
2. Run: `pytest tests/test_ui_playwright.py -v`
3. Document results in report

---

## 12. Time Estimates

**Planning your final push:**

| Task | Time Estimate |
|------|---------------|
| Run all tests and verify results | 15 minutes |
| Capture all screenshots | 20 minutes |
| Complete REPORT.md | 1-2 hours |
| Create SLIDES (PowerPoint) | 2-3 hours |
| Export to PDF | 15 minutes |
| Organize deliverables | 30 minutes |
| Create ZIP and submit | 15 minutes |
| **TOTAL** | **5-7 hours** |

**Recommended schedule:**
- **Day 1:** Run tests, capture screenshots, verify artifacts (1 hour)
- **Day 2:** Complete report (2 hours)
- **Day 3:** Create presentation (3 hours)
- **Day 4:** Export, organize, submit (1 hour)

---

## 13. Contact & Support

**If you have questions:**

1. **Check this guide first** - Most common issues are covered
2. **Review tool documentation** - Links in VV_README.md
3. **Check course forums** - Other students may have same questions
4. **Contact instructor** - Use course email or office hours

**Include in your help request:**
- What step you're on
- What error message you're seeing (exact text)
- What you've already tried
- Screenshots of the issue

---

## Summary Checklist

Quick reference for what needs to be done:

```
□ Run all tests successfully
□ Capture 2-3 key screenshots (coverage dashboard, pytest output, UI)
□ Complete REPORT.md (fill in names, dates, insert screenshots)
□ Export REPORT.md to REPORT.pdf
□ Create SLIDES from SLIDES.md (PowerPoint or PDF)
□ Organize files into VV_Project_Submission folder
□ Create ZIP archive
□ Submit via Microsoft Teams
□ Keep backup copy
□ Prepare for presentation (if required)
```

---

**You've got this! Good luck with your submission! 🚀**

If you have any questions about these instructions, ask before the deadline!

---

**Last Updated:** October 30, 2025
**Version:** 1.0
**Authors:** Claude Code AI Assistant
