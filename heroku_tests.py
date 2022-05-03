from playwright.sync_api import Playwright, sync_playwright, expect
# Drag and drop
def heroku_tests(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to http://the-internet.herokuapp.com/
    page.goto("http://the-internet.herokuapp.com/")
    # Click text=Drag and Drop
    page.locator("text=Drag and Drop").click()
    # expect(page).to_have_url("http://the-internet.herokuapp.com/drag_and_drop")
    # Click html
    page.locator("html").click()
    # Click html
    page.locator("html").click()
   

 # Download file
    page.locator("text=File Download").first.click()
    # expect(page).to_have_url("http://the-internet.herokuapp.com/download")
    # Click text=img.png
    with page.expect_download() as download_info:
        page.locator("text=img.png").click()
    download = download_info.value
    # expect(page).to_have_url("http://the-internet.herokuapp.com/download")

# Drop down
    # Select 1
    page.locator("select").select_option("1")
    # Select 2
    page.locator("select").select_option("2")
    # ---------------------

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(heroku_tests)