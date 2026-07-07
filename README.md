# QA Automation Test Task (Playwright + Pytest)

Automated UI test suite for [The Internet Herokuapp](https://herokuapp.com) built using Python 3.13, Pytest, Playwright, and the Page Object Model (POM) pattern.

## Project Structure
```text
├── .github/workflows/    # CI/CD GitHub Actions configuration
├── configs/              # Environment configuration loader
│   └── config.py
├── pages/                # Page Object classes (locators & actions)
│   ├── base_page.py
│   ├── main_page.py
│   ├── login_page.py
│   └── security_page.py
├── tests/                # Pytest automation scenarios
│   ├── main_page.py             # Scenario 1: Links and elements checks
│   ├── test_invalid_login.py    # Scenario 2: Parametrized negative login tests
│   └── valid_login.py           # Scenario 3: Positive login/logout flow
├── .env.example          # Template for local environment variables
├── .gitignore            # Git exclusion rules
├── conftest.py           # Pytest core fixtures
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Prerequisites
Ensure **Python 3.13** is installed on your local machine.

## Local Installation

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone <your-repository-url>
   cd <repository-folder-name>
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   # Activate on macOS/Linux:
   source .venv/bin/activate
   # Activate on Windows (CMD):
   .venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Chromium browser:**
   ```bash
   playwright install chromium
   ```

5. **Configure Environment Variables:**
   Create a `.env` file in the root directory. You can copy the structure from `.env.example` or use the template below:
   
   ```text
   BASE_URL=https://herokuapp.com
   VALID_USER=tomsmith
   VALID_PASS=SuperSecretPassword!
   ```
   *Note: The `.env` file is included in `.gitignore` and will remain strictly local.*


## Running Tests

### Run the entire test suite:
```bash
pytest
```

### Environment-Dependent Approach (Changing Base URL)
To override the default URL dynamically on the fly without changing the `.env` file, change the `BASE_URL` variable in your terminal before execution [сторонняя ссылка]:

**macOS / Linux:**
```bash
BASE_URL=https://your-alternative-url.com pytest
```

**Windows (CMD):**
```cmd
set BASE_URL=https://your-alternative-url.com && pytest
```

**Windows (PowerShell):**
```powershell
\$env:BASE_URL="https://your-alternative-url.com"; pytest
```
