from core.browser import Browser

browser = Browser()

print("Launching Chrome...")

browser.launch_chrome()

input(
    "\nLog into Yard Commander.\n"
    "When you are looking at the site press ENTER..."
)

browser.connect()

browser.goto_edit()

print("SUCCESS!")

input("\nPress ENTER to exit...")

browser.disconnect()