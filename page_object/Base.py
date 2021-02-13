from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, *locator):
        return self.driver.find_element(*locator)

    def _existing_of_elements(self, *locator):
        return len(self.driver.find_elements(*locator)) == 1

    def _click(self, *locator):
        ActionChains(self.driver).move_to_element(self.__element(*locator)).click().perform()

    def _wait_for_visible(self, *locator, wait=5):
        element = self.driver.find_element(*locator)
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(element))
