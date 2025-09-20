import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     choices=['ar',
                              'en',
                              'ca',
                              'cs',
                              'da',
                              'de',
                              'en-gb',
                              'el',
                              'es',
                              'fi',
                              'fr',
                              'it',
                              'ko',
                              'nl',
                              'pl',
                              'pt',
                              'pt-br',
                              'ro',
                              'ru',
                              'sk',
                              'uk',
                              'zh-hans'],
                     help='Choose language: \nar - ,العربيّة'
                          '\nen - English'
                          '\nca - català,'
                          '\ncs - česky,'
                          '\nda - dansk,'
                          '\nde - Deutsch,'
                          '\nen-gb - British English,'
                          '\nel - Ελληνικά,'
                          '\nes - español,'
                          '\nfi - suomi,'
                          '\nfr - français,'
                          '\nit - italiano,'
                          '\nko - 한국어,'
                          '\nnl - Nederlands,'
                          '\npl - polski,'
                          '\npt - Português,'
                          '\npt-br - Português Brasileiro,'
                          '\nro - Română,'
                          '\nru - Русский,'
                          '\nsk - Slovensky,'
                          '\nuk - Українська,'
                          '\nzh-hans - 简体中文',)


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    print(f"\nTesting with language: {language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser')
    browser.quit()
