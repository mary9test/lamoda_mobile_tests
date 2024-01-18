from lamoda_mobile_tests_framework.pages.menu_page import menu
import allure


@allure.title("Отображение элементов меню")
@allure.tag("web_tests")
@allure.feature("menu_page")
@allure.severity('critical')
def test_menu_button_title(context):
    menu.catalog_button_is_displayed()
    menu.main_page_button_is_displayed()
    menu.basket_button_is_displayed()
    menu.favourites_button_is_displayed()
    menu.sign_in_page_button_is_displayed()
