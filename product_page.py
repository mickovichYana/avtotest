from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        )
        button.click()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_text(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_text(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_be_add_to_basket_message(self, expected_name):
        success_message = self.get_success_message_text()
        assert expected_name in success_message, \
            f"Product name '{expected_name}' not in message '{success_message}'"

    def should_be_correct_basket_total(self, expected_price):
        basket_total = self.get_basket_total_text()
        assert expected_price == basket_total, \
            f"Expected price '{expected_price}', got '{basket_total}'"