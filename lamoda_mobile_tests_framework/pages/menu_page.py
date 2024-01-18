from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
import allure


class MenuPage:

    def catalog_button_is_displayed(self):
        with allure.step("Кнопка Каталог отображается"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Каталог"]')).should(
                have.text(
                    'Каталог'))

    def main_page_button_is_displayed(self):
        with allure.step("Кнопка Главная отображается"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Главная"]')).should(
                have.text(
                    'Главная'))

    def basket_button_is_displayed(self):
        with allure.step("Кнопка Корзина отображается"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Корзина"]')).should(
                have.text(
                    'Корзина'))

    def favourites_button_is_displayed(self):
        with allure.step("Кнопка Избранное отображается"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Избранное"]')).should(
                have.text(
                    'Избранное'))

    def sign_in_page_button_is_displayed(self):
        with allure.step("Кнопка Войти отображается"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Войти"]')).should(
                have.text(
                    'Войти'))


menu = MenuPage()
