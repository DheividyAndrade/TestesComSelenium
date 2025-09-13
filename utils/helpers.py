import time
import random

def wait(seconds=2):
    """Espera fixa (somente para visualização, prefira WebDriverWait em produção)."""
    time.sleep(seconds)

def random_name():
    nomes = ["João", "Maria", "Carlos", "Ana", "Paulo"]
    return random.choice(nomes)

def random_lastname():
    sobrenomes = ["Silva", "Souza", "Oliveira", "Costa", "Ferreira"]
    return random.choice(sobrenomes)

def random_zip():
    return str(random.randint(10000, 99999))
