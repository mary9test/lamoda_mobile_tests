from lamoda_mobile_tests_framework.pages.catalog_page import catalog
import allure


@allure.title("Соответствие названий разделов в каталоге")
@allure.tag("mobile_tests")
@allure.feature("catalog_page")
@allure.severity('critical')
def test_catalog_section_title(context):
    catalog.catalog_button_click()
    catalog.scroll_down_mobile_page()
    catalog.go_to_brands_section()
    catalog.verify_section_title_name_all_brands()
    catalog.verify_section_title_name_premium()
    catalog.verify_section_title_name_favourites()
