import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.chrome.options import Options as Chrome_Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, en, es ...")
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    browser = None
    if browser_name == "chrome":
        options = Chrome_Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options_firefox = Firefox_Options()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
    yield browser
    print("\nquit browser..")
    browser.quit()
