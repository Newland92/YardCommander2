from pathlib import Path

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

CHROME_PROFILE = PROJECT_ROOT / "ChromeProfile"

# ------------------------------------------------------------------
# Chrome
# ------------------------------------------------------------------

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

DEBUG_PORT = 9222

DEBUG_URL = f"http://127.0.0.1:{DEBUG_PORT}"

# ------------------------------------------------------------------
# Yard Commander
# ------------------------------------------------------------------

BASE_URL = "https://ymx-kroger.yardcommander.com"

EDIT_URL = f"{BASE_URL}/edit"

# ------------------------------------------------------------------
# Timeouts
# ------------------------------------------------------------------

CONNECT_TIMEOUT = 30
PAGE_TIMEOUT = 15000

HEADLESS = False