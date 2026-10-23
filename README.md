# DemoQA Selenium Automation

Automated UI tests for selected components on [DemoQA](https://demoqa.com/), implemented with Python, Selenium WebDriver, and pytest.

The suite follows the Page Object Model (POM): test cases describe user behavior and assertions, while page-object classes contain locators and browser interactions. Each test receives a fresh Chrome browser through the shared pytest fixture.

## Features covered

The current suite contains 12 tests covering 10 DemoQA feature areas:

| Test module | Feature | Coverage |
| --- | --- | --- |
| `tests/test_01_text_box.py` | Text Box | Enters name, email, current address, and permanent address; submits the form; verifies the output |
| `tests/test_02_checkbox.py` | Check Box | Expands the tree, selects a checkbox, and verifies the result text |
| `tests/test_03_radio_button.py` | Radio Button | Selects `Yes`, then `Impressive`, and verifies the selected result changes |
| `tests/test_04_web_tables.py` | Web Tables | Adds a record, verifies the row count increases, deletes a record, and verifies the row count decreases |
| `tests/test_05_buttons.py` | Buttons | Verifies double-click, right-click, and dynamic single-click messages |
| `tests/test_06_alerts.py` | Alerts | Covers simple, confirm, and prompt JavaScript alerts |
| `tests/test_07_upload.py` | Upload/Download | Uploads `test_data/sample_file.txt` and verifies the displayed file name |
| `tests/test_08_date_picker.py` | Date Picker | Enters `12/25/2025` and verifies the date field value |
| `tests/test_09_drag_drop.py` | Droppable | Drags the source element into the target and verifies `Dropped!` |
| `tests/test_10_practice_form.py` | Practice Form | Fills required form fields and verifies the confirmation modal |

The alert feature is represented by three tests, so the total collection count is 12 rather than 10.

## Requirements

- Windows, macOS, or Linux
- Python 3.8 or newer
- Google Chrome installed
- Internet access while tests run
- Access to `https://demoqa.com/`

The project currently pins these Python packages in [`requirements.txt`](requirements.txt):

- `selenium==4.17.2`
- `pytest==7.4.3`
- `webdriver-manager==4.0.1`
- `pytest-html==4.1.1`

`webdriver-manager` downloads and manages a compatible ChromeDriver when needed. The first run can therefore take longer and requires network access.

## Installation

Open PowerShell in the project directory:

```powershell
cd C:\Users\nandu\Downloads\DemoQA
```

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, either allow scripts for the current user or invoke the environment's Python directly:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the tests

### Recommended command

Run the complete suite and generate the self-contained HTML report:

```powershell
$env:PYTHONUTF8 = "1"
python .\run_all_tests.py
```

The UTF-8 environment setting is recommended on Windows because the tests print `✓` and the runner prints `✗`. Without UTF-8 output enabled, the default CP1252 console can raise `UnicodeEncodeError` even after the browser interaction itself succeeds.

The runner:

1. Discovers tests under `tests/`.
2. Runs pytest in verbose mode.
3. Shows test print output.
4. Uses short tracebacks.
5. Writes a self-contained report to [`test_report.html`](test_report.html).
6. Returns pytest's exit code to the operating system.

### Run pytest directly

Run all tests without the custom runner:

```powershell
$env:PYTHONUTF8 = "1"
python -m pytest tests\ -v --tb=short -s
```

Run one module:

```powershell
python -m pytest tests\test_06_alerts.py -v -s
```

Run one test:

```powershell
python -m pytest tests\test_01_text_box.py::TestTextBox::test_text_box_submission -v -s
```

Generate an HTML report directly with pytest:

```powershell
$env:PYTHONUTF8 = "1"
python -m pytest tests\ -v --tb=short -s --html=test_report.html --self-contained-html
```

## Expected result

A successful run ends with output similar to:

```text
======================= 12 passed ========================
Exit Code: 0
Status: ✓ ALL TESTS PASSED
```

The test suite interacts with a live external website, so execution time depends on network speed, DemoQA availability, browser startup, and page-load behavior. A complete run has recently taken approximately four minutes.

## Project structure

```text
DemoQA/
├── pages/                         # Page Object Model classes
│   ├── base_page.py               # Shared waits, scrolling, clicking, and text entry
│   ├── alerts_page.py
│   ├── buttons_page.py
│   ├── checkbox_page.py
│   ├── date_picker_page.py
│   ├── drag_drop_page.py
│   ├── practice_form_page.py
│   ├── radio_button_page.py
│   ├── text_box_page.py
│   ├── upload_page.py
│   └── web_tables_page.py
├── tests/                         # pytest test cases
│   ├── conftest.py                # Browser fixture and session messages
│   └── test_*.py
├── test_data/
│   └── sample_file.txt            # Upload-test input
├── screenshots/                   # Screenshots retained by the project
├── utils/
│   └── helpers.py                 # Reusable wait, scrolling, and screenshot helpers
├── requirements.txt
├── run_all_tests.py               # Main suite runner
├── test_report.html               # Generated pytest HTML report
└── README.md
```

Python bytecode directories such as `__pycache__` and pytest's `.pytest_cache` are generated during execution and are not part of the test design.

## Test architecture

### Browser fixture

[`tests/conftest.py`](tests/conftest.py) defines a function-scoped `driver` fixture. For every test it:

- Creates a new Chrome WebDriver.
- Starts Chrome maximized.
- Disables selected automation banners, popups, and notifications.
- Attempts to install or locate ChromeDriver through `webdriver-manager`.
- Falls back to Selenium's automatic driver discovery if the managed-driver setup fails.
- Sets a 30-second page-load timeout.
- Sets a five-second implicit wait.
- Quits the browser during teardown.

The function scope keeps tests isolated from browser state left by earlier tests.

### Page objects

Most tests instantiate a page object and call methods such as `open`, `fill_form`, `click_*`, or `get_*`. Common behavior is inherited from [`pages/base_page.py`](pages/base_page.py), including:

- Explicit waits using `WebDriverWait`.
- Visibility and clickability checks.
- Scrolling elements into view before interaction.
- Clearing and entering text.
- Reading visible text.
- Safe visibility checks that return `False` after a timeout.

The drag-and-drop test currently performs its interaction directly in [`tests/test_09_drag_drop.py`](tests/test_09_drag_drop.py), because it needs an `ActionChains` sequence and additional explicit waits for the draggable and droppable elements.

### Test style

Tests use an Arrange/Act/Assert structure:

1. Create a page object and test data.
2. Open the target page and perform user actions.
3. Assert visible page state or result content.

Test data is intentionally defined close to the test that uses it, which makes each scenario readable and independent.

## Reports and generated files

The custom runner overwrites [`test_report.html`](test_report.html) on each run. Open it in a browser after execution to inspect:

- Pass/fail status for each test.
- Duration.
- Captured output.
- Failure tracebacks.
- Environment and plugin metadata.

The upload test ensures that `test_data/sample_file.txt` exists before uploading it. If the file is missing, the test recreates it with sample content.

## Troubleshooting

### `UnicodeEncodeError` mentioning `cp1252` or `charmap`

Run with UTF-8 enabled:

```powershell
$env:PYTHONUTF8 = "1"
python .\run_all_tests.py
```

This is a console-output issue caused by the checkmark and cross characters in test and runner messages. It is not evidence that the browser assertion failed.

### ChromeDriver or browser startup failure

Check that:

1. Google Chrome is installed and can start normally.
2. The installed Chrome version is supported by the available driver.
3. The machine can reach the driver download service.
4. No existing Chrome process or security policy prevents WebDriver startup.
5. Dependencies are installed in the Python interpreter being used:

```powershell
python -m pip show selenium webdriver-manager pytest
```

If the managed driver cannot be downloaded, install a compatible ChromeDriver or restore network access and rerun.

### Timeout, stale element, or click-interception failures

DemoQA is a live site and includes advertisements and dynamic content. Before rerunning:

- Confirm `https://demoqa.com/` is reachable in Chrome.
- Close unexpected modal dialogs or browser extensions.
- Avoid running multiple browser-heavy test sessions simultaneously.
- Rerun the affected test in isolation to determine whether the issue is reproducible.

For example:

```powershell
python -m pytest tests\test_09_drag_drop.py -v -s
```

The drag-and-drop test intentionally waits for the page elements and adds short delays around scrolling and animation.

### Tests fail because the website changed

The tests use locators and page behavior from the current DemoQA pages. If the site changes its DOM:

1. Reproduce the failure with the individual test.
2. Update the corresponding page object in `pages/`.
3. Keep test assertions focused on user-visible behavior.
4. Rerun the affected test, then the full suite.

Prefer changing locators and interaction methods in page objects rather than duplicating Selenium code in tests.

## Adding a new test

1. Add or update a page object in `pages/`.
2. Put reusable interaction methods in the page object.
3. Add a numbered test module under `tests/`.
4. Use the existing `driver` fixture.
5. Assert observable behavior rather than implementation details.
6. Run the new test in isolation.
7. Run the full suite and inspect `test_report.html`.

Example command for a new module:

```powershell
python -m pytest tests\test_11_new_feature.py -v -s
```

## Maintenance guidance

- Keep dependency versions in [`requirements.txt`](requirements.txt) synchronized with the environment used to run the suite.
- Prefer explicit waits for dynamic elements and avoid increasing global sleeps unless a specific page behavior requires it.
- Keep browser setup and teardown centralized in `tests/conftest.py`.
- Keep locators and page-specific actions in `pages/`.
- Treat the generated HTML report and pytest cache as run artifacts, not source code.
- Because the suite depends on an external website, include the browser version, Python version, and test report when diagnosing failures.

## Current verification

The complete suite was last verified with:

- Python 3.14.2
- pytest 7.4.3
- Selenium 4.17.2
- pytest-html 4.1.1
- Windows 11
- Chrome WebDriver

Result: **12 passed, 0 failed**.
