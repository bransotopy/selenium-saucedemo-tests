"""
LoginPage
---------
Representa la página de inicio de sesión de SauceDemo (https://www.saucedemo.com/).
Hereda de BasePage los métodos genéricos (click, type_text, etc.).
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # --- Locators: dónde están los elementos en el HTML de la página ---
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # --- Acciones que se pueden hacer en esta página ---

    def load(self):
        """Abre la página de login en el navegador."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        """Escribe usuario y contraseña, y hace clic en el botón de login."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Retorna el texto del mensaje de error (si aparece)."""
        return self.get_text(self.ERROR_MESSAGE)
    
