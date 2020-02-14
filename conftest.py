import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="with this option choose browser you use to make tests \
                          'chrome' for Google Chrome, 'firefox' for FireFox")
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="choose local language with this option:\
                          you may choose among 'ru','en', etc..")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    usr_language = request.config.getoption('language')
    browser = None
    if browser_name =='chrome':
        print('\nstarting Chrome browser for testing..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': usr_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstarting FireFox browser for testing..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', usr_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('"--browser_name" parameter has to be "chrome" or "ffox"')
    yield browser
    print('\nquit browser..')
    browser.quit()
