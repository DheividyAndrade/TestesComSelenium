import pytest
from pages.login_page import LoginPage

def test_login_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("usuario_teste", "senha_teste")

    assert "Dashboard" in driver.title
