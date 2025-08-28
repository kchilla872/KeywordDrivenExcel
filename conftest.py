import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            allure.attach(page.screenshot(), name="screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="function", autouse=True)
def allure_test_setup():
    with allure.step("Test setup"):
        yield
    with allure.step("Test teardown"):
        pass
