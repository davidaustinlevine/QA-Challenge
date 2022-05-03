# QA-Challenge

Simple functional  Playwright tests written in Python (with pytest) 
Requirements:
    Python 3.7 or above 
    nodeJS v11 or higher
    Playwright 1.18 or higher 
    Windows Subsystem for Linux (WSL)
    macOS == 10.14 (Mojave or higher)


Installation:
Node.js --
    macOS
    brew install node

    Android 
    pkg install nodejs

    Windows
    Download installer directly from the node.js web site
     
     or

     Using Winget:
     winget install OpenJS.NodeJS
     # or for LTS
     winget install OpenJS.NodeJS.LTS

     Using Chocolatey:
     cinst nodejs
     # or for full install with npm
     cinst nodejs.install

Playwright --
    Python
    pip install --upgrade pip
    pip install pytest-playwright
    

    nodeJS
    npm i -D @playwright/test
    # install supported browsers
    npx playwright install

Usage:
    Once installed, you can import Playwright in a Python script, and launch any of the 3 browsers (chromium, firefox and webkit):

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        browser.close()

Running:
Run all tests in the suite

    macOS (pytest CLI)
    pytest
 
    Windows
    npx playwright { directory }
