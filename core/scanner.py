from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from core.models import Trailer


class Scanner:

    def __init__(self, browser, logger=None):
        self.browser = browser
        self.logger = logger
        self.page = browser.get_page()

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    def log(self, message):
        print(message)

        if self.logger:
            try:
                self.logger.write(message)
            except Exception:
                pass

    # ---------------------------------------------------------
    # Scan Yard
    # ---------------------------------------------------------

    def scan(self):

        trailers = []

        self.log("Starting yard scan...")

        while True:

            rows = self.page.locator("table tbody tr")

            count = rows.count()

            self.log(f"Found {count} trailers on page.")

            for i in range(count):

                row = rows.nth(i)

                cells = row.locator("td")

                if cells.count() < 6:
                    continue

                try:

                    trailer = Trailer(
                        trailer=cells.nth(0).inner_text().strip(),
                        status=cells.nth(1).inner_text().strip(),
                        contents=cells.nth(2).inner_text().strip(),
                        tractor=cells.nth(3).inner_text().strip(),
                        po=cells.nth(4).inner_text().strip(),
                        seal=cells.nth(5).inner_text().strip(),
                    )

                    trailers.append(trailer)

                except Exception as ex:
                    self.log(f"Error reading row {i + 1}: {ex}")

            # ---------------------------------------------
            # Next Page
            # ---------------------------------------------

            try:

                next_button = self.page.get_by_role(
                    "button",
                    name="Next"
                )

                if not next_button.is_enabled():
                    break

                next_button.click()

                self.page.wait_for_load_state("networkidle")

            except PlaywrightTimeoutError:
                break

            except Exception:
                break

        self.log(f"Scan complete. {len(trailers)} trailers found.")

        return trailers