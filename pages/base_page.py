"""
BasePage
--------
Clase padre del patrón Page Object Model (POM).
Contiene métodos genéricos y reutilizables que todas las páginas
específicas (LoginPage, InventoryPage, etc.) heredarán.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Clase base de la que heredan todas las páginas del sitio."""

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Espera a que un elemento exista en el DOM y lo retorna."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        """Espera a que existan elementos y retorna la lista completa."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """
        Espera a que un elemento sea clickeable y hace click sobre él.
        Si el clic nativo de Selenium no surte efecto (a veces pasa por temas
        de renderizado), se usa un clic vía JavaScript como respaldo.
        """
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)

    def type_text(self, locator, text):
        """Limpia un campo de texto y escribe el valor indicado."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """Retorna el texto visible de un elemento."""
        return self.find(locator).text

    def is_visible(self, locator) -> bool:
        """Retorna True si el elemento es visible en pantalla."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def current_url(self) -> str:
        """Retorna la URL actual del navegador."""
        return self.driver.current_url 
    
    def click_and_wait_for_url(self, locator, url_fragment: str, retries: int = 2):
        """
        Hace clic en un elemento y espera a que la URL contenga cierto texto,
        reintentando el clic si la navegación no ocurre a tiempo (esto cubre
        pequeñas inconsistencias de renderizado/carga del sitio bajo prueba).
        """
        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.support import expected_conditions as EC

        ultimo_error = None
        for intento in range(retries):
            self.click(locator)
            try:
                self.wait.until(EC.url_contains(url_fragment))
                return
            except TimeoutException as e:
                ultimo_error = e
                continue
        raise ultimo_error
    