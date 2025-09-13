import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    # Caminho para o msedgedriver.exe
    service = Service(r"C:\Users\deivi\Downloads\edgedriver_win32\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)

    yield driver
    driver.quit()
