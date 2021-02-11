from page_object.MainPage import MainPage


def test_check_elements_on_main_page(browser):
    MainPage(browser).check_existing_of_logo()
    MainPage(browser).check_existing_of_search()
    MainPage(browser).check_existing_of_currency()
    MainPage(browser).check_existing_about_us()
    MainPage(browser).check_existing_of_wish_list()
