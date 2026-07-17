"""
conftest.py
-----------
Archivo especial que pytest detecta automáticamente.
Aquí definimos "fixtures": código reutilizable que se ejecuta
antes y/o después de cada prueba (en este caso, abrir y cerrar Chrome).
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Fixture que crea una instancia de Chrome antes de cada prueba,
    la entrega a la prueba (yield), y la cierra automáticamente al terminar.
    """
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()

    yield drv  # <-- aquí la prueba recibe el navegador y hace su trabajo

    drv.quit()  # <-- esto se ejecuta automáticamente al terminar la prueba 