"""
test_login.py
--------------
Casos de prueba relacionados con el inicio de sesión en SauceDemo.
"""

from pages.login_page import LoginPage


def test_login_exitoso(driver):
    """
    Caso de prueba 1: Login exitoso con credenciales válidas.
    Se espera que el usuario sea redirigido a la página de inventario.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_login_usuario_bloqueado(driver):
    """
    Caso de prueba 2: Login con usuario bloqueado.
    Se espera un mensaje de error indicando que el usuario está bloqueado.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    mensaje = login_page.get_error_message()
    assert "locked out" in mensaje.lower()


def test_login_credenciales_incorrectas(driver):
    """
    Caso de prueba 3: Login con contraseña incorrecta.
    Se espera un mensaje de error genérico.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "clave_incorrecta")

    mensaje = login_page.get_error_message()
    assert "do not match" in mensaje.lower() 
    
