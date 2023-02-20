from selene import have
from selene.support.shared import browser


def test_example():
    browser.config.timeout = 10.0
    browser.open('https://www.python.org/')
    browser.element('li#downloads > a').click()
    browser.element('div.download-unknown > h1.call-to-action').should(
        have.text('Download the latest version of Python'))
    browser.quit()
