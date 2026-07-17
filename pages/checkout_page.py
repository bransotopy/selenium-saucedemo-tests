"""
CheckoutPage
------------
Representa el proceso de checkout (finalizar compra) de SauceDemo.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # --- Locators ---
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    # --- Acciones ---

    def go_to_checkout(self):
        """Hace clic en el botón 'Checkout' desde el carrito."""
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Completa el formulario de datos de envío."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_purchase(self):
        """
        Hace clic en el botón final 'Finish' para completar la compra.
        Incluye un reintento automático ante posibles fallos de
        sincronización en el primer clic.
        """
        from selenium.common.exceptions import TimeoutException

        for intento in range(2):
            self.click(self.FINISH_BUTTON)
            try:
                self.wait.until(EC.url_contains("checkout-complete"))
                return
            except TimeoutException:
                if intento == 0:
                    continue
                raise

    def get_confirmation_message(self) -> str:
        """Retorna el mensaje de confirmación tras completar la compra."""
        return self.get_text(self.COMPLETE_HEADER)
    
    