from lamoda_mobile_tests_framework.pages.catalog_page import catalog
from lamoda_mobile_tests_framework.utils.helpers import skip_initial_screens
import allure


@allure.title("Соответствие названий разделов в каталоге")
@allure.tag("mobile_tests")
@allure.feature("catalog_page")
@allure.severity('critical')
def test_catalog_section_title(context):
    skip_initial_screens()
    catalog.catalog_button_click()
    catalog.scroll_down_mobile_page()
    catalog.go_to_brands_section()
    catalog.verify_section_title_name_all_brands()
    catalog.verify_section_title_name_premium()
    catalog.verify_section_title_name_favourites()
