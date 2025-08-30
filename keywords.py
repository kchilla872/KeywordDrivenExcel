def openurl(page, url):
    page.goto(url)


def click(page, locator):

    page.wait_for_selector(locator, timeout=10000, state='visible')
    page.locator(locator).scroll_into_view_if_needed()
    page.click(locator)


def inputtext(page, locator, text):
    page.locator(locator).fill(str(text))


def waitforelement(page, locator, timeout=5000):
    page.wait_for_selector(locator, timeout=int(timeout))


def shoppingcart(page, locator):
    page.wait_for_selector(locator, timeout=10000)
    page.locator(locator).scroll_into_view_if_needed()
    page.click(locator)


def select(page, locator, value):
    element = page.wait_for_selector(locator, timeout=10000, state='visible')
    element.select_option(value=str(value))


def check_checkbox(page, locator):
    checkbox = page.locator(locator)
    checkbox.check()
