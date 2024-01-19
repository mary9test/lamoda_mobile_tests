import allure
import pytest
import allure_commons
from lamoda_mobile_tests_framework.utils import allure_attach
from lamoda_mobile_tests_framework.utils.helpers import abs_path
from dotenv import load_dotenv
from selene import browser, support
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--context", default="bstack", help="Specify context")


def pytest_configure(config):
    context = config.getoption("--context")
    dotenv_path = abs_path(f'.env.{context}')
    load_dotenv(dotenv_path=dotenv_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import settings
    options = settings.to_driver_options(context=context)

    with allure.step('init app session'):
        if settings.remote_url is not None:
            browser.config.driver = webdriver.Remote(
                settings.remote_url,
                options=options
            )
        else:
            raise ValueError("Remote URL is not specified in the settings.")

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    allure_attach.attach_bstack_screenshot()
    allure_attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if context == 'bstack':
        allure_attach.attach_bstack_video(settings, session_id)

    browser.quit()
