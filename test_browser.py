from core.browser_manager import BrowserManager


def main():
    browser = BrowserManager()

    try:
        browser.launch()

        input("\nPress ENTER after Chrome has opened and you are logged in...")

        browser.connect()
        browser.goto_edit()

        print("\nSUCCESS!")
        print("Browser Manager is working correctly.")

        input("\nPress ENTER to close...")

    finally:
        browser.disconnect()


if __name__ == "__main__":
    main()