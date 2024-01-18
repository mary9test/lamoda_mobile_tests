from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
import allure


class CatalogPage:

    def catalog_button_click(self):
        with allure.step("Переходим в каталог"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Каталог"]')).click()

    def go_to_brands_section(self):
        with allure.step("Заходим в раздел Бренды"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Бренды"]')).click()

    def scroll_down_mobile_page(self):
        with allure.step("Скроллим экран вниз"):
            screen_size = browser.driver.get_window_size()
            screen_width = screen_size['width']
            screen_height = screen_size['height']

            start_x = int(screen_width / 2)
            start_y = int(screen_height * 0.8)
            end_y = int(screen_height * 0.2)
            browser.driver.swipe(start_x, start_y, start_x, end_y, 400)

    def verify_section_title_name_all_brands(self):
        with allure.step("Проверяем название раздела Все бренды"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Все бренды"]')).should(have.text("Все бренды"))

    def verify_section_title_name_premium(self):
        with allure.step("Проверяем название раздела Премиум"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Премиум"]')).should(have.text("Премиум"))

    def verify_section_title_name_favourites(self):
        with allure.step("Проверяем название раздела Любимые"):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView[@text="Любимые"]')).should(have.text("Любимые"))


catalog = CatalogPage()
