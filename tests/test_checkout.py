from pages.checkout_page import CheckoutPage

def test_finalizar_compra(driver):
    checkout = CheckoutPage(driver)
    checkout.open()
    checkout.realizar_checkout("produto_teste")

    assert "Pedido confirmado" in checkout.get_confirmation_text()
