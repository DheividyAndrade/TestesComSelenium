import time
import random
from selenium.webdriver.common.by import By

def wait(seconds=2):
    """Espera fixa (não recomendado para produção, melhor usar WebDriverWait)."""
    time.sleep(seconds)

def random_email():
    """Gera um e-mail fake para cadastro ou testes."""
    return f"teste_{random.randint(1000,9999)}@exemplo.com"

def random_username():
    """Gera um usuário fake."""
    return f"user_{random.randint(1000,9999)}"

def element_exists(driver, locator: tuple) -> bool:
    """Verifica se um elemento existe na página."""
    try:
        driver.find_element(*locator)
        return True
    except:
        return False
