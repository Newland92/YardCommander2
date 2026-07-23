import subprocess
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

from config import (
    CHROME_PATH,
    CHROME_PROFILE,
    DEBUG_PORT,
    DEBUG_URL,
    EDIT_URL,
)


class Browser:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    # ---------------------------------------------------------
    # Launch Chrome
    # ---------------------------------------------------------

    def launch_chrome(self):

        if not Path(CHROME_PATH).exists():
            raise FileNotFoundError(
                f"Chrome executable not found:\n{CHROME_PATH}"
            )

        print("Launching Chrome...")

        subprocess.Popen(
            [
                CHROME_PATH,
                f"--remote-debugging-port={DEBUG_PORT}",
                f"--user-data-dir={CHROME_PROFILE}",
                "--new-window",
                EDIT_URL,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    # ---------------------------------------------------------
    # Connect to Chrome
    # ---------------------------------------------------------

    def connect(self):

        if self.playwright is None:
            self.playwright = sync_playwright().start()

        print("Waiting for Chrome...")

        while True:

            try:

                self.browser = (
                    self.playwright.chromium.connect_over_cdp(
                        DEBUG_URL
                    )
                )

                break

            except Exception:

                time.sleep(1)

        if self.browser.contexts:
            self.context = self.browser.contexts[0]
        else:
            self.context = self.browser.new_context()

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        print("Connected!")

    # ---------------------------------------------------------
    # Navigate to Edit Page
    # ---------------------------------------------------------

    def goto_edit(self):

        print("Opening Edit page...")

        self.page.goto(EDIT_URL)

        self.page.wait_for_load_state("networkidle")

        print("Ready.")

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def get_page(self):
        return self.page

    def reconnect(self):
        self.connect()
        self.goto_edit()

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def disconnect(self):

        try:
            if self.browser:
                self.browser.close()
        except Exception:
            pass

        try:
            if self.playwright:
                self.playwright.stop()
        except Exception:
            pass