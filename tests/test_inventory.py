"""
test_inventory.py
------------------
Casos de prueba relacionados con la página de inventario/productos.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def _login_como_standard_user(driver):
    """
    Función auxiliar (no es un test): hace login antes de cada prueba
    de inventario, ya que para llegar ahí siempre hay que iniciar sesión primero.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")


def test_agregar_producto_al_carrito(driver):
    """
    Caso de prueba 4: Agregar un producto al carrito.
    Se espera que el contador del carrito muestre "1".
    """
    _login_como_standard_user(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_quitar_producto_del_carrito(driver):
    """
    Caso de prueba 5: Agregar y luego quitar un producto del carrito.
    Se espera que el contador desaparezca (vuelva a "0", es decir, sin badge).
    """
    _login_como_standard_user(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.get_cart_count() == "0"


def test_ordenar_productos_por_precio(driver):
    """
    Caso de prueba 6: Ordenar productos de menor a mayor precio.
    Se espera que la lista de precios quede en orden ascendente.
    """
    _login_como_standard_user(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.sort_by_price_low_to_high()
    precios_texto = inventory_page.get_all_prices()

    # Convertimos "$9.99" -> 9.99 (número) para poder compararlos
    precios_numeros = [float(p.replace("$", "")) for p in precios_texto]

    assert precios_numeros == sorted(precios_numeros)
    
    