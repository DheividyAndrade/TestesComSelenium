from utils.helpers import wait, random_email

def test_cadastro(driver):
    driver.get("https://exemplo.com/cadastro")
    
    driver.find_element("id", "email").send_keys(random_email())
    driver.find_element("id", "username").send_keys("teste")
    driver.find_element("id", "password").send_keys("123456")
    driver.find_element("id", "register").click()

    wait(3)  # só para ver a página antes de fechar
    assert "Bem-vindo" in driver.page_source
