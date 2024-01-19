from lamoda_mobile_tests_framework.pages.menu_page import menu
from lamoda_mobile_tests_framework.utils.helpers import skip_initial_screens
import allure


@allure.title("Отображение элементов меню")
@allure.tag("mobile_tests")
@allure.feature("menu_page")
@allure.severity('critical')
def test_menu_button_title(context):
    skip_initial_screens()
    menu.catalog_button_is_displayed()
    menu.main_page_button_is_displayed()
    menu.basket_button_is_displayed()
    menu.favourites_button_is_displayed()
    menu.sign_in_page_button_is_displayed()
