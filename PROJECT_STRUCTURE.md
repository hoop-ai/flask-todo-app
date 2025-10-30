# Project Structure - Complete File Overview

Visual guide to all files in your V&V project.

---

## 📁 Complete Directory Tree

```
flask-todo-app/
│
├── 📖 START_HERE.md                    ⭐ READ THIS FIRST - Navigation guide
├── 📖 QUICK_REFERENCE.md               ⭐ One-page cheat sheet
├── 📖 SUBMISSION_GUIDE.md              ⭐ Detailed submission instructions (13 sections)
├── 📖 VV_README.md                     ⭐ Setup & troubleshooting guide
├── 📖 REPORT.md                        ✏️ FILL IN: Your V&V report (export to PDF)
├── 📖 SLIDES.md                        ✏️ FILL IN: Presentation outline (export to PDF)
├── 📖 PROJECT_STRUCTURE.md             📋 This file - shows all files
│
├── 🐍 app.py                           ✅ Flask application (modified for testing)
├── 🐍 domain_contracts.py              ✅ Business logic contracts (icontract)
├── 🐍 conftest.py                      ✅ Pytest configuration
├── 📝 Makefile                         ✅ Convenience commands (make all, make test, etc.)
├── 📝 requirements.txt                 ✅ Original Flask app dependencies
│
├── 📂 tests/                           ⭐ TEST SUITE (3 files)
│   ├── test_api_properties.py          ✅ Functional + property-based tests (Hypothesis)
│   ├── test_contracts.py               ✅ Runtime contract verification
│   └── test_ui_playwright.py           ✅ UI E2E tests with screenshot capture
│
├── 📂 artifacts/                       ⭐ TEST ARTIFACTS (auto-generated)
│   ├── coverage.xml                    ✅ Coverage report (Cobertura format, ~6 KB)
│   ├── junit.xml                       ✅ Test results (JUnit format, ~3 KB)
│   └── ui_after_add.png                ✅ UI screenshot (959 KB) 📸
│
├── 📂 htmlcov/                         ⭐ COVERAGE HTML REPORT
│   ├── index.html                      ✅ Main coverage dashboard (open in browser)
│   ├── status.json                     ✅ Coverage metadata
│   └── [many other HTML files]         ✅ Per-file coverage details
│
├── 📂 screenshots/                     📸 YOUR SCREENSHOTS (you create this)
│   ├── coverage_dashboard.png          📸 TO CREATE: Screenshot of htmlcov/index.html
│   ├── pytest_output.png               📸 TO CREATE: Screenshot of pytest -v output
│   ├── swagger_ui.png                  📸 OPTIONAL: Screenshot of /apidocs
│   └── app_ui_home.png                 📸 OPTIONAL: Screenshot of app homepage
│
├── 📂 templates/                       🌐 Flask HTML templates (original app)
│   └── index.html                      🌐 Homepage template
│
├── 📂 static/                          🎨 CSS/JS files (if any, original app)
│
├── 📂 .venv/                           🚫 Virtual environment (DO NOT submit)
│   └── [Python packages]               🚫 Excluded from submission (too large)
│
├── 📂 .pytest_cache/                   🚫 Pytest cache (auto-generated)
├── 📂 __pycache__/                     🚫 Python cache (auto-generated)
├── 🗄️ todo.db                          🚫 SQLite database (auto-generated)
├── 📝 .coverage                        🚫 Coverage data file (auto-generated)
└── 📝 README.md                        📖 Original app README (optional to keep)
```

---

## 📊 Files by Category

### 📖 Documentation (Read & Edit)

| File | Status | Action Required |
|------|--------|----------------|
| START_HERE.md | ✅ Complete | **Read first** - navigation guide |
| QUICK_REFERENCE.md | ✅ Complete | Use as cheat sheet |
| SUBMISSION_GUIDE.md | ✅ Complete | Follow step-by-step |
| VV_README.md | ✅ Complete | Reference for setup/troubleshooting |
| **REPORT.md** | ✏️ **Edit** | **Fill in:** names, dates, screenshots |
| **SLIDES.md** | ✏️ **Edit** | **Fill in:** visuals, team info |
| PROJECT_STRUCTURE.md | ✅ Complete | This file (reference) |

---

### 🧪 Test Suite (Complete - Don't Edit)

| File | Purpose | Lines | Tests |
|------|---------|-------|-------|
| tests/test_api_properties.py | Functional + Hypothesis property tests | 44 | 3 tests (100+ Hypothesis cases) |
| tests/test_contracts.py | icontract runtime verification | 3 | 1 test |
| tests/test_ui_playwright.py | Playwright browser automation | 18 | 1 test + screenshot |
| domain_contracts.py | Contract definitions for CrossHair | 8 | N/A (verified by CrossHair) |
| conftest.py | Pytest shared configuration | 6 | N/A (configuration) |

**Total:** 5 test functions, 100+ generated test cases

---

### 🎯 Artifacts (Auto-Generated - Don't Edit)

| File | Format | Size | Purpose |
|------|--------|------|---------|
| artifacts/coverage.xml | XML (Cobertura) | ~6 KB | For CI/CD integration |
| artifacts/junit.xml | XML (JUnit) | ~3 KB | Test results for dashboards |
| artifacts/ui_after_add.png | PNG image | 959 KB | Visual proof of UI test |
| htmlcov/index.html | HTML | ~50 KB | Interactive coverage report |
| htmlcov/*.html | HTML | Various | Per-file coverage details |

**How to view:**
- XML files: Open in text editor or CI/CD tool
- PNG file: `start artifacts\ui_after_add.png`
- HTML files: `start htmlcov\index.html`

---

### 📸 Screenshots (You Need to Create)

| Screenshot | Where to Get It | Filename | Required? |
|------------|-----------------|----------|-----------|
| Coverage Dashboard | Open `htmlcov/index.html`, screenshot | coverage_dashboard.png | ⭐ REQUIRED |
| Pytest Output | Run `pytest -v`, screenshot terminal | pytest_output.png | ⭐ RECOMMENDED |
| UI Screenshot | Already done! At `artifacts/ui_after_add.png` | ui_after_add.png | ✅ DONE |
| Swagger API Docs | Open `/apidocs`, screenshot | swagger_ui.png | Optional |
| App Homepage | Open `/`, screenshot | app_ui_home.png | Optional |

**See:** [SUBMISSION_GUIDE.md - Section 1](SUBMISSION_GUIDE.md#1-getting-all-screenshots) for detailed instructions

---

### 🐍 Source Code (Modified for V&V)

| File | Original? | Changes Made | Purpose |
|------|-----------|--------------|---------|
| app.py | Modified | Added `if __name__ == "__main__"` wrapper | Prevents app.run() on import (fixes pytest) |
| domain_contracts.py | **NEW** | N/A | Business logic with icontract decorators |
| conftest.py | **NEW** | N/A | Pytest configuration for imports |
| Makefile | **NEW** | N/A | Convenience commands |

---

## 🎯 What You Need for Submission

### ⭐ Required Files (Must Include)

```
✅ docs/
   ├── REPORT.pdf               (your filled-in report)
   ├── SLIDES.pdf               (your presentation)
   └── VV_README.md             (setup instructions)

✅ tests/
   ├── test_api_properties.py   (functional + property tests)
   ├── test_contracts.py        (contract tests)
   └── test_ui_playwright.py    (UI E2E tests)

✅ src/
   ├── app.py                   (Flask app)
   ├── domain_contracts.py      (contracts)
   ├── conftest.py              (pytest config)
   └── Makefile                 (commands)

✅ artifacts/
   ├── coverage.xml             (coverage data)
   ├── junit.xml                (test results)
   ├── ui_after_add.png         (UI screenshot)
   └── htmlcov/
       └── index.html           (coverage HTML)

✅ screenshots/
   ├── coverage_dashboard.png   (coverage view)
   └── pytest_output.png        (test results)
```

---

### 🚫 Exclude from Submission

```
🚫 DO NOT INCLUDE:
   .venv/                       (too large, ~200 MB)
   __pycache__/                 (auto-generated)
   .pytest_cache/               (auto-generated)
   .coverage                    (binary file, XML is enough)
   todo.db                      (test database)
   node_modules/                (if you used npm)
   *.pyc                        (compiled Python)
```

---

## 📏 File Sizes Reference

| Item | Approximate Size |
|------|------------------|
| **Documentation (MD)** | 500 KB total |
| **Documentation (PDF)** | 2-5 MB total |
| **Test Code** | 10 KB |
| **Source Code** | 20 KB |
| **Artifacts (XML)** | 10 KB |
| **Screenshots** | 2-3 MB |
| **htmlcov/** | 500 KB |
| **Total (with .venv)** | ~250 MB |
| **Total (without .venv)** | ~10-15 MB ✅ |

**ZIP file should be: < 20 MB**

---

## 🔍 How to Find Files

### On Windows:

```bash
# Navigate to project
cd "C:\Users\User\OneDrive\Downloads\Uni\Project - Software Validation\Tasks\flask-todo-app"

# List all key files
dir /B *.md
dir /B tests\*.py
dir /B artifacts\*.*

# Open files
start START_HERE.md
start QUICK_REFERENCE.md
code REPORT.md
```

### On macOS/Linux:

```bash
# Navigate to project
cd flask-todo-app

# List all key files
ls -lh *.md
ls -lh tests/*.py
ls -lh artifacts/*

# Open files
open START_HERE.md
open QUICK_REFERENCE.md
code REPORT.md
```

---

## 🗺️ Navigation Flow

```
START_HERE.md
    ↓
    ├─→ QUICK_REFERENCE.md (for fast reference)
    │
    └─→ SUBMISSION_GUIDE.md (for detailed instructions)
            ↓
            ├─→ Section 1: Getting Screenshots
            ├─→ Section 3: Completing REPORT.md
            ├─→ Section 4: Creating SLIDES
            ├─→ Section 5: Exporting to PDF
            └─→ Section 6-8: Organizing & Submitting
```

**Stuck?** → VV_README.md (troubleshooting)

---

## 🎓 File Usage Guide

### When Writing Your Report:

**Reference these:**
- `artifacts/coverage.xml` → Copy coverage numbers
- `artifacts/junit.xml` → Copy test results
- `screenshots/coverage_dashboard.png` → Insert image
- `screenshots/pytest_output.png` → Insert image
- `artifacts/ui_after_add.png` → Insert image

**From these:**
- `REPORT.md` → Template with structure

---

### When Creating Your Presentation:

**Reference these:**
- `SLIDES.md` → Outline with speaker notes
- `screenshots/*` → All images
- `artifacts/ui_after_add.png` → UI demo

**Create:**
- PowerPoint or Google Slides (14 slides)
- Or use Marp/Pandoc to convert SLIDES.md

---

### When Running Tests:

**Execute these:**
- `Makefile` → Run `make all`
- Or individual commands:
  ```bash
  pytest -v
  coverage run -m pytest
  crosshair check domain_contracts.py
  ```

**Generates these:**
- `.coverage` → Coverage data
- `artifacts/coverage.xml` → Coverage export
- `artifacts/junit.xml` → Test results
- `htmlcov/` → HTML report

---

## 📋 Quick Checklist

Use this to track your progress:

```
FILE PREPARATION:
□ START_HERE.md read
□ QUICK_REFERENCE.md bookmarked
□ SUBMISSION_GUIDE.md read (at least Sections 1, 3, 6)
□ Screenshots captured (coverage_dashboard.png, pytest_output.png)
□ REPORT.md filled in (names, dates, screenshots)
□ SLIDES created (PowerPoint or PDF)
□ REPORT.pdf exported
□ SLIDES.pdf exported

FILE ORGANIZATION:
□ Created VV_Project_Submission/ folder
□ Copied all required files
□ Created submission README
□ Excluded .venv/ and cache folders
□ Created ZIP file
□ ZIP file < 50 MB
□ Tested ZIP extraction

SUBMISSION:
□ Opened Microsoft Teams
□ Navigated to SEN4013 course
□ Found Assignments area
□ Uploaded ZIP file
□ Added submission message
□ Received confirmation
□ Saved backup copy
```

---

## 💡 Tips for Finding Files

### "Where is the coverage report?"
- **Interactive HTML:** `htmlcov/index.html` (open in browser)
- **XML data:** `artifacts/coverage.xml` (for CI/CD)
- **Terminal:** Run `coverage report -m`

### "Where is the UI screenshot?"
- **Already captured:** `artifacts/ui_after_add.png`
- **View:** `start artifacts\ui_after_add.png` (Windows)

### "Where do I put my screenshots?"
- **Create folder:** `screenshots/`
- **Save here:**
  - `screenshots/coverage_dashboard.png`
  - `screenshots/pytest_output.png`
  - `screenshots/swagger_ui.png` (optional)

### "Which files do I edit?"
- **Only edit:**
  - `REPORT.md` → Fill in names, dates, screenshots
  - `SLIDES.md` → Add team info, create presentation
- **Don't edit:**
  - Test files (already complete)
  - Artifacts (auto-generated)
  - app.py (already modified)

### "What files do I submit?"
- **See:** [QUICK_REFERENCE.md - Files to Submit](QUICK_REFERENCE.md#-files-to-submit)
- **Or:** [SUBMISSION_GUIDE.md - Section 6](SUBMISSION_GUIDE.md#6-organizing-deliverables)

---

## 🎯 At a Glance Summary

| Category | Count | Total Size | Status |
|----------|-------|------------|--------|
| **Documentation** | 7 MD files | 500 KB | ✅ Complete (2 need editing) |
| **Test Files** | 5 files | 10 KB | ✅ Complete |
| **Artifacts** | 4 items | 1.5 MB | ✅ Generated |
| **Screenshots** | 2-5 images | 2-3 MB | 📸 You need to capture |
| **PDFs (to create)** | 2 files | 3-6 MB | ✏️ Need to export |

**Everything is ready except:**
1. Capture 2 screenshots (15 minutes)
2. Fill in REPORT.md (30 minutes)
3. Create SLIDES (2 hours)
4. Export to PDF (15 minutes)
5. Organize & submit (30 minutes)

**Total remaining work: ~4-5 hours**

---

## 🚀 Next Steps

1. **Read:** [START_HERE.md](START_HERE.md) (this gives you the roadmap)
2. **Skim:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (5-min overview)
3. **Follow:** [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md) (step-by-step)
4. **Reference:** This file when you need to find something

---

**You're all set! Everything is organized and ready to go.** 🎉

Need to find a file? Refer to the directory tree at the top.
Need to do something? Check [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md).
Need a quick answer? Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md).

**Good luck with your submission!** 🚀
