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


class BrowserManager:
    def __init__(self, logger=None):
        self.logger = logger

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    # ---------------------------------------------------------
    # Logging Helper
    # ---------------------------------------------------------

    def log(self, message):
        print(message)

        if self.logger:
            try:
                self.logger.write(message)
            except Exception:
                pass

    # ---------------------------------------------------------
    # Launch Chrome
    # ---------------------------------------------------------

    def launch(self):

        if not Path(CHROME_PATH).exists():
            raise FileNotFoundError(
                f"Chrome executable not found:\n{CHROME_PATH}"
            )

        self.log("Launching Chrome...")

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
    # Connect
    # ---------------------------------------------------------

    def connect(self, timeout=30):

        if self.playwright is None:
            self.playwright = sync_playwright().start()

        self.log("Waiting for Chrome...")

        start = time.time()

        while time.time() - start < timeout:

            try:

                self.browser = self.playwright.chromium.connect_over_cdp(
                    DEBUG_URL
                )

                if self.browser.contexts:
                    self.context = self.browser.contexts[0]
                else:
                    self.context = self.browser.new_context()

                if self.context.pages:
                    self.page = self.context.pages[0]
                else:
                    self.page = self.context.new_page()

                self.log("Connected!")

                return

            except Exception:
                time.sleep(1)

        raise TimeoutError(
            f"Unable to connect to Chrome after {timeout} seconds."
        )

    # ---------------------------------------------------------
    # Navigate
    # ---------------------------------------------------------

    def goto_edit(self):

        if not self.is_connected():
            raise RuntimeError("Browser is not connected.")

        self.log("Opening Edit page...")

        self.page.goto(EDIT_URL)

        self.page.wait_for_load_state("networkidle")

        self.log("Edit page loaded.")

    # ---------------------------------------------------------
    # Convenience
    # ---------------------------------------------------------

    def reconnect(self):
        self.connect()
        self.goto_edit()

    def get_page(self):
        return self.page

    def get_context(self):
        return self.context

    def get_browser(self):
        return self.browser

    def is_connected(self):
        return (
            self.browser is not None
            and self.context is not None
            and self.page is not None
        )

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def disconnect(self):

        self.log("Disconnecting...")

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

        self.page = None
        self.context = None
        self.browser = None
        self.playwright = None

        self.log("Disconnected.")