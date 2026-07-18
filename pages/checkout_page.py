"""
CheckoutPage
------------
Representa el proceso de checkout (finalizar compra) de SauceDemo.
"""

from selenium.webdriver.common.by import By
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
        """Completa el formulario de datos de envío y avanza a la página de resumen."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_and_wait_for_url(self.CONTINUE_BUTTON, "checkout-step-two")

    def finish_purchase(self):
        """Hace clic en el botón final 'Finish' para completar la compra."""
        self.click_and_wait_for_url(self.FINISH_BUTTON, "checkout-complete")

    def get_confirmation_message(self) -> str:
        """Retorna el mensaje de confirmación tras completar la compra."""
        return self.get_text(self.COMPLETE_HEADER)
    
    