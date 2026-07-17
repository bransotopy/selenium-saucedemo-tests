"""
InventoryPage
-------------
Representa la página de inventario/catálogo de productos de SauceDemo
(la página que aparece justo después de hacer login).
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # --- Locators ---
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    # --- Acciones ---

    def add_backpack_to_cart(self):
        """Agrega la mochila 'Sauce Labs Backpack' al carrito."""
        self.click(self.ADD_TO_CART_BACKPACK)

    def remove_backpack_from_cart(self):
        """Quita la mochila del carrito (desde la misma página de inventario)."""
        self.click(self.REMOVE_BACKPACK)

    def get_cart_count(self) -> str:
        """Retorna el número que se muestra en el ícono del carrito."""
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def go_to_cart(self):
        """Hace clic en el ícono del carrito para ir a esa página."""
        self.click(self.CART_LINK)

    def sort_by_price_low_to_high(self):
        """Selecciona la opción 'Price (low to high)' en el dropdown de orden."""
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value("lohi")

    def get_all_prices(self) -> list:
        """Retorna una lista de precios (como texto) de todos los productos visibles."""
        elementos = self.find_all(self.PRODUCT_PRICES)
        return [el.text for el in elementos] 
    
    