from core.browser_manager import BrowserManager


def main():

    browser = BrowserManager()

    try:
        browser.launch()

        input(
            "\nPress ENTER after Chrome opens and you are logged into Yard Commander..."
        )

        browser.connect()
        browser.goto_edit()

        page = browser.get_page()

        rows = page.locator("table tbody tr")

        print("\n" + "=" * 80)
        print("COLUMN DEBUG")
        print("=" * 80)

        row_count = min(rows.count(), 3)

        for r in range(row_count):

            print(f"\nROW {r + 1}")
            print("-" * 80)

            cells = rows.nth(r).locator("td")

            for c in range(cells.count()):

                text = cells.nth(c).inner_text().strip()

                print(f"Column {c}: {text}")

        print("\nDone.")

        input("\nPress ENTER to exit...")

    finally:
        browser.disconnect()


if __name__ == "__main__":
    main()