import allure
import allure_commons
import pytest
from selene import support
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose one language from: ru, en, es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()

    # browser.config._wait_decorator = support._logging.wait_with(
    #     context=allure_commons._allure.StepContext
    # )
    #
    # yield
    #
    # allure.attach(
    #     browser.driver.get_screenshot_as_png(),
    #     name='screenshot',
    #     attachment_type=allure.attachment_type.PNG,
    # )
    # browser.quit()