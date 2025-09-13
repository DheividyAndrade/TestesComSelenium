from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def open_and_add_product(self):
        self.visit("https://www.saucedemo.com/inventory.html")
        self.click(self.ADD_TO_CART)
        self.click(self.CART_BUTTON)

    def checkout(self, first, last, zip_code):
        self.click(self.CHECKOUT_BUTTON)
        self.type(self.FIRST_NAME_INPUT, first)
        self.type(self.LAST_NAME_INPUT, last)
        self.type(self.POSTAL_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)
        self.click(self.FINISH_BUTTON)

    def get_confirmation_text(self):
        return self.find(self.CONFIRMATION).text
