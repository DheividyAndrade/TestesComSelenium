from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    PRODUCT_INPUT = (By.ID, "product")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONFIRMATION_TEXT = (By.ID, "confirmation")

    def open(self):
        self.visit("https://exemplo.com/checkout")

    def realizar_checkout(self, produto):
        self.type(self.PRODUCT_INPUT, produto)
        self.click(self.CHECKOUT_BUTTON)

    def get_confirmation_text(self):
        return self.find(self.CONFIRMATION_TEXT).text
