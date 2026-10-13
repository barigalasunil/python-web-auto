# FYC Web-Only Framework

A Python + Playwright + pytest-bdd framework for web-only test automation. This framework has been migrated away from device-based automation (Roku, Android, iOS, Appium) to a pure web approach.

## Prerequisites

- Python 3.x
- Playwright browsers installed

## Installation

```batch
:: 1. Create and activate a virtual environment
py -m venv .venv
call .venv\Scripts\activate

:: 2. Install dependencies
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m playwright install chromium
```

## Execution

Run the desired test suite using the `py run.py` entry point:

```batch
:: Smoke test (runs the login smoke test)
py run.py smoke

:: Sanity test
py run.py sanity

:: Regression test
py run.py regression
```

## Test Results & Artifacts

Every test run creates a uniquely timestamped directory under `test-results/`:

```
test-results/
  2026-10-12_15-30-45_smoke/
  │
  ├── allure-results/        (Allure JSON files for test metadata)
  ├── logs/
  │   ├── execution.log      (Custom execution-aware logger output)
  │   └── errors.log         (Error log)
  │
  ├── reports/
  │   ├── report.html        (Self-contained HTML report via pytest-html)
  │   └── report.pdf         (Rendered PDF via Playwright page.pdf())
  │
  ├── screenshots/
  │   ├── passed/            (Screenshots of passing tests)
  │   └── failed/            (Screenshots of failing tests)
  │
  ├── traces/                (Test trace files, if enabled)
  │
  └── reports/               (Convenience copy of report.html and report.pdf)
```

### Viewing Reports

- **HTML Report**: Open `test-results/<timestamp>_smoke/reports/report.html` in any browser, or open the copy at `reports/report.html` (generated at workspace root).
- **PDF Report**: Open `test-results/<timestamp>_smoke/reports/report.pdf` in any PDF viewer, or open the copy at `reports/report.pdf` (generated at workspace root).

## Framework Structure

The framework follows a clean, industry-standard layout:

```
project_root/
  ├── features/              (All .feature files, web-only BDD scenarios)
  ├── steps/                 (All pytest-bdd step definitions)
  ├── pages/                 (Playwright Page Objects, web-only)
  ├── components/            (Reusable UI components, if any)
  ├── utils/                 (logger.py, artifact_manager.py, reporting.py)
  ├── config/                (environments.json, pytest.ini)
  ├── test-results/          (Dynamically created per run, add to .gitignore)
  ├── .venv/                 (Virtual environment, add to .gitignore)
  ├── run.py                 (Single entry point: `py run.py smoke`)
  ├── requirements.txt
  └── README.md
```

## FY037 Fix Summary

The FY037 step `Verify Email Input Field Is Not Present` previously had a bug where `self.locators["EMAIL_INPUT_FIELD"]` key was missing from the page object's locators dictionary. The `except Exception` blanket-catch silently converted `KeyError` into "field absent", causing the assertion to always pass regardless of the field's actual state.

**Fix applied:**
1. Added `EMAIL_INPUT_FIELD: (".//input[@name='username']")` to the `locators` dictionary (reuses the existing `CLIENT_EMAIL_FIELD` selector)
2. Changed `except Exception: return False` → `except TimeoutError: return False` so that `KeyError` now propagates as a test failure instead of being silently swallowed

## Known Artifacts

The framework generates the following per-run artifacts:

- `test-results/<timestamp>_smoke_smoke/logs/execution.log`
- `test-results/<timestamp>_smoke_smoke/logs/errors.log`
- `test-results/<timestamp>_smoke_smoke/allure-results/` (per-test JSON metadata)
- `test-results/<timestamp>_smoke_smoke/reports/report.html` (pytest-html)
- `test-results/<timestamp>_smoke_smoke/reports/report.pdf` (Playwright-rendered PDF)
- `test-results/<timestamp>_smoke_smoke/screenshots/` (passed/failed screenshots)
- `test-results/<timestamp>_smoke_smoke/traces/` (trace files)

## .gitignore

The following are typically gitignored:

```
# Dependencies
.venv/

# Test results (dynamically created per run)
test-results/

# Local reporter directories
reports/
allure-results/
```