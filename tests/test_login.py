from pages.login_page import LoginPage

def test_login_sucesso(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    
    assert "inventory" in driver.current_url
