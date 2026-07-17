"""
test_checkout.py
-----------------
Caso de prueba del flujo completo de compra (checkout).
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_completar_compra_exitosa(driver):
    """
    Caso de prueba 7: Flujo completo de compra.
    Se espera el mensaje "Thank you for your order!" al finalizar.
    """
    # Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Agregar producto y pasar al carrito
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # Checkout
    checkout_page = CheckoutPage(driver)
    checkout_page.go_to_checkout()
    checkout_page.fill_checkout_info("Bran", "Solis", "12345")
    checkout_page.finish_purchase()


    mensaje = checkout_page.get_confirmation_message()
    assert "thank you for your order" in mensaje.lower() 
    
    