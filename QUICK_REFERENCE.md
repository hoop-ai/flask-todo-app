# Quick Reference Guide
## One-Page Cheat Sheet for V&V Project

---

## 🚀 Quick Start (Copy & Paste)

```bash
# Terminal 1: Start Flask
cd flask-todo-app
.venv\Scripts\activate
python app.py

# Terminal 2: Run all tests
cd flask-todo-app
.venv\Scripts\activate
make all
```

---

## 📸 Screenshots Needed

### 1. Coverage Dashboard (REQUIRED) ⭐
```bash
start htmlcov\index.html
# Press Win+Shift+S to screenshot
# Save as: screenshots/coverage_dashboard.png
```
**Shows:** 67% coverage, file list

---

### 2. UI Screenshot (ALREADY DONE) ✅
```bash
# Already captured at:
artifacts/ui_after_add.png

# To view:
start artifacts\ui_after_add.png
```
**Shows:** "Buy milk" todo added via browser

---

### 3. Pytest Output (RECOMMENDED) 📊
```bash
pytest -v
# Screenshot the terminal output
# Save as: screenshots/pytest_output.png
```
**Shows:** 4 passed, 1 failed

---

## 📁 Files to Submit

### Required Files (Must Include)
```
✅ docs/REPORT.pdf               (your completed report)
✅ docs/SLIDES.pdf               (your presentation)
✅ docs/VV_README.md             (setup instructions)
✅ tests/test_api_properties.py  (functional + property tests)
✅ tests/test_contracts.py       (contract tests)
✅ tests/test_ui_playwright.py   (UI E2E tests)
✅ artifacts/coverage.xml        (coverage data)
✅ artifacts/junit.xml           (test results)
✅ artifacts/ui_after_add.png    (UI screenshot)
✅ htmlcov/index.html            (coverage HTML report)
```

### Optional But Recommended
```
📷 screenshots/coverage_dashboard.png
📷 screenshots/pytest_output.png
📝 SUBMISSION_GUIDE.md (this guide)
```

---

## ✏️ What to Fill In

### In REPORT.md:
1. Replace `[Your Names Here]` with team names
2. Replace `January 16, 2026` with submission date
3. Insert screenshot: `![Coverage](screenshots/coverage_dashboard.png)`
4. Review all sections, remove any `[PLACEHOLDER]` text

### In SLIDES.md:
1. Add team names on Slide 1
2. Add visuals (screenshots, logos)
3. Review speaker notes

---

## 🔄 Complete Workflow (30 minutes)

### Step 1: Verify Tests (5 min)
```bash
cd flask-todo-app
.venv\Scripts\activate
pytest -v
# Expected: 4 passed, 1 failed ✓
```

### Step 2: Get Screenshots (10 min)
```bash
# Coverage HTML
start htmlcov\index.html
# Screenshot → Save to screenshots/

# Pytest output
pytest -v
# Screenshot terminal → Save to screenshots/

# UI (already done)
start artifacts\ui_after_add.png
```

### Step 3: Complete Report (5 min)
```bash
# Open in editor
code REPORT.md

# Find & Replace:
[Your Names Here] → Your Actual Names
January 16, 2026 → Today's Date

# Save
```

### Step 4: Export to PDF (5 min)
```bash
# Option 1: Pandoc
pandoc REPORT.md -o REPORT.pdf --toc

# Option 2: VS Code Markdown PDF extension
# Right-click REPORT.md → Markdown PDF: Export (pdf)
```

### Step 5: Create Submission Folder (5 min)
```bash
cd ..
mkdir VV_Project_Submission

# Copy key files (see "Files to Submit" above)
cp flask-todo-app/REPORT.pdf VV_Project_Submission/docs/
cp flask-todo-app/SLIDES.pdf VV_Project_Submission/docs/
# ... (see SUBMISSION_GUIDE.md for full list)

# Create ZIP
Compress-Archive VV_Project_Submission VV_Project_YourNames.zip
```

### Step 6: Submit via Teams
1. Open Microsoft Teams
2. Navigate to SEN4013 course
3. Go to Assignments
4. Upload `VV_Project_YourNames.zip`
5. Add submission message (see SUBMISSION_GUIDE.md)

---

## 🐛 The Bug You Found

**INC-001: Missing Title Length Validation**

**Quick Test:**
```bash
curl -X POST http://127.0.0.1:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"'"$(python -c "print('x'*200)")"'"}'

# Returns: HTTP 201 ✗ (should be 400)
```

**Why it matters:**
- Shows V&V discovered a real defect
- Demonstrates value of negative testing
- Good story for your presentation

---

## 📊 Key Numbers to Know

| Metric | Value | What it Means |
|--------|-------|---------------|
| Tests | 5 total | Comprehensive coverage |
| Passed | 4 (80%) | Core functionality works |
| Failed | 1 (expected) | Bug discovered (INC-001) |
| Coverage | 67% | Good for initial V&V |
| Tools | 6 used | Multi-faceted approach |
| Hypothesis Cases | 100+ | Property-based edge cases |

---

## 🛠️ Troubleshooting Quick Fixes

### Flask won't start
```bash
# Check if already running
netstat -ano | findstr :5000

# Kill if needed
taskkill /PID <PID> /F
```

### Tests won't run
```bash
# Ensure venv activated
.venv\Scripts\activate

# Reinstall if needed
pip install -r requirements.txt
pip install pytest hypothesis coverage playwright icontract crosshair-tool
```

### Screenshots missing
```bash
# Re-run UI test
pytest tests/test_ui_playwright.py -v

# Re-generate coverage
coverage run -m pytest
coverage html
start htmlcov\index.html
```

---

## 📚 Full Guides

- **Detailed Instructions:** [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md) (13 sections, 500+ lines)
- **Setup & Run:** [VV_README.md](VV_README.md)
- **Full Report Template:** [REPORT.md](REPORT.md)
- **Presentation Outline:** [SLIDES.md](SLIDES.md)

---

## ⏰ Time Management

| Task | Time |
|------|------|
| Verify tests work | 15 min |
| Capture screenshots | 20 min |
| Complete REPORT.md | 1-2 hours |
| Create slides | 2-3 hours |
| Export to PDF | 15 min |
| Organize & submit | 45 min |
| **TOTAL** | **5-7 hours** |

---

## ✅ Final Checklist

Before submitting, verify:

- [ ] Tests run successfully (4 passed, 1 failed)
- [ ] `htmlcov/index.html` opens and shows 67%
- [ ] `artifacts/ui_after_add.png` exists and is viewable
- [ ] REPORT.pdf has your names and date
- [ ] SLIDES.pdf includes visuals
- [ ] Screenshots captured (minimum 2)
- [ ] ZIP file created and < 50MB
- [ ] Submitted via Microsoft Teams
- [ ] Backup copy saved

---

## 🎯 Grading Quick Check

| Section | Points | What You Have |
|---------|--------|---------------|
| Tool Review | 35 pts | ✅ 6 tools documented in REPORT.md |
| Test Results | 35 pts | ✅ All 6 test types completed |
| Report | 20 pts | ✅ REPORT.md template (fill in names/dates) |
| Presentation | 10 pts | ✅ SLIDES.md outline (add visuals) |

---

## 💡 Pro Tips

1. **Highlight the bug** - INC-001 shows V&V works
2. **Use visuals** - Screenshots make reports professional
3. **Follow speaker notes** - They're pre-written for you
4. **Test on fresh machine** - Ensure ZIP extracts properly
5. **Submit early** - Avoid last-minute tech issues

---

## 📞 Need Help?

1. Check [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md) - Detailed troubleshooting
2. Check [VV_README.md](VV_README.md) - Setup issues
3. Re-read tool docs - Links in VV_README.md
4. Contact instructor - Include error messages

---

**Quick Command Reference:**

```bash
# Run everything
make all

# Just tests
pytest -v

# Just coverage
coverage run -m pytest && coverage report

# Just UI test
pytest tests/test_ui_playwright.py -v

# Just formal verification
crosshair check domain_contracts.py

# View coverage
start htmlcov\index.html

# View UI screenshot
start artifacts\ui_after_add.png
```

---

**Good luck! 🚀 You've got this!**

Everything is already set up and working. Just capture screenshots, fill in your names, export to PDF, and submit!
