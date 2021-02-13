from page_object.AdminPage import AdminPage


def test_existing_elements_on_admin_page(browser, url):
    admin_url = url + '/admin'
    browser.get(admin_url)
    AdminPage(browser).admin_page_check_existing_of_username_input()
    AdminPage(browser).admin_page_check_existing_of_password_input()
    AdminPage(browser).admin_page_check_existing_of_login_button()
    AdminPage(browser).admin_page_check_existing_of_forgotten_password_button()
    AdminPage(browser).admin_page_check_existing_of_logo()


def test_check_settings_modal_window_on_admin_page(browser, url):
    admin_url = url + '/admin'
    browser.get(admin_url)
    AdminPage(browser).wait_for_logo_on_login_page()
    AdminPage(browser).click_on_login_button()
    AdminPage(browser).wait_for_navigation_title_on_admin_page()
    AdminPage(browser).click_on_settings_button()
    AdminPage(browser).check_existing_of_title_setting_modal_window()


def test_check_calendar_on_sales_analytics_block_on_admin_page(browser, url):
    admin_url = url + '/admin'
    browser.get(admin_url)
    AdminPage(browser).wait_for_logo_on_login_page()
    AdminPage(browser).click_on_login_button()
    AdminPage(browser).wait_for_navigation_title_on_admin_page()
    AdminPage(browser).click_on_calendar()
    AdminPage(browser).check_existing_of_drop_down_calendar_menu()


def test_check_demo_login_and_logout_on_admin_page(browser, url):
    admin_url = url + '/admin'
    browser.get(admin_url)
    AdminPage(browser).wait_for_logo_on_login_page()
    AdminPage(browser).click_on_login_button()
    AdminPage(browser).wait_for_navigation_title_on_admin_page()
    AdminPage(browser).check_existing_of_demo_login()
    AdminPage(browser).click_on_logout_button()
    AdminPage(browser).wait_for_logo_on_login_page()
    AdminPage(browser).admin_page_check_existing_of_logo()


def test_check_product_table(browser, url):
    admin_url = url + '/admin'
    browser.get(admin_url)
    AdminPage(browser).wait_for_logo_on_login_page()
    AdminPage(browser).click_on_login_button()
    AdminPage(browser).wait_for_navigation_title_on_admin_page()
    AdminPage(browser).click_on_catalog_menu()
    AdminPage(browser).click_on_product_menu()
    AdminPage(browser).check_existing_of_products_link()
