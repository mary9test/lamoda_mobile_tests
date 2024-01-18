from lamoda_mobile_tests_framework.pages.kids_section_page import kids
import allure


@allure.title("Соответствие названий разделов")
@allure.tag("web_tests")
@allure.feature("kids_section_page")
@allure.severity('critical')
def test_kids_section_title(context):
    kids.catalog_button_click()
    kids.kids_section_click()
    kids.verify_elements_in_kids_section()
