from lamoda_mobile_tests_framework.pages.kids_section_page import kids
from lamoda_mobile_tests_framework.utils.helpers import skip_initial_screens
import allure


@allure.title("Соответствие названий разделов в секции Дети")
@allure.tag("mobile_tests")
@allure.feature("kids_section_page")
@allure.severity('critical')
def test_kids_section_title(context):
    skip_initial_screens()
    kids.catalog_button_click()
    kids.kids_section_click()
    kids.verify_elements_in_kids_section()
