from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
import allure


class KidsPage:
    def catalog_button_click(self):
        with allure.step("Переходим в каталог"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Каталог"]')).click()

    def kids_section_click(self):
        with allure.step("Переходим в раздел дети"):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Детям"]')).click()

    def verify_elements_in_kids_section(self):
        with allure.step("Проверяем названия разделов"):
            elements_to_verify = ["Девочкам", "Мальчикам", "Малышам", "Игрушки"]
            for element_text in elements_to_verify:
                browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{element_text}"]')).should(
                    have.text(element_text))


kids = KidsPage()
