from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from utils.helpers import random_name, random_lastname, random_zip

def test_finalizar_compra(driver):
    # Login primeiro
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Checkout
    checkout = CheckoutPage(driver)
    checkout.open_and_add_product()
    checkout.checkout(random_name(), random_lastname(), random_zip())

    assert "Thank you for your order!" in checkout.get_confirmation_text()
