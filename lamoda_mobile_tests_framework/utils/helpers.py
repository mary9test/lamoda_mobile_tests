import os
from selene import browser

from appium.webdriver.common.appiumby import AppiumBy
from pathlib import Path
import lamoda_mobile_tests_framework


def abs_path(path: str):
    return (
        Path(lamoda_mobile_tests_framework.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )


def skip_initial_screens():
    browser.element(
        (AppiumBy.XPATH, '//android.widget.RadioButton[@resource-id="com.lamoda.lite:id/russiaButton"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.lamoda.lite:id/button"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.lamoda.lite:id/dismiss"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.lamoda.lite:id/dismiss"]')).click()
