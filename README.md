# Actividad de Automatización de Pruebas — SauceDemo
# Calidad del Software
# Simulación: Mi primera ejecución de pruebas

Proyecto académico de automatización de pruebas funcionales utilizando **Selenium WebDriver** con Python, aplicando el patrón de diseño **Page Object Model (POM)**.

## Sitio bajo prueba
[SauceDemo](https://www.saucedemo.com/) — sitio de demostración autorizado para practicar automatización de pruebas.

## Tecnologías utilizadas
- Python 3.12
- Selenium WebDriver 4.23.1
- Pytest 8.3.2
- Pytest-HTML (generación de reportes)
- WebDriver Manager (gestión automática del ChromeDriver)

## Estructura del proyecto
selenium-saucedemo-tests/
├── pages/              # Clases del patrón Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/               # Casos de prueba
│   ├── conftest.py
│   ├── test_login.py
│   └── test_inventory.py
├── reports/             # Informes HTML generados
├── requirements.txt
└── pytest.ini

## Casos de prueba implementados
1. Login exitoso con credenciales válidas
2. Login con usuario bloqueado
3. Login con credenciales incorrectas
4. Agregar producto al carrito
5. Quitar producto del carrito
6. Ordenar productos por precio (menor a mayor)

## Cómo ejecutar el proyecto

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pytest -v --html=reports/informe.html --self-contained-html
```

## Autor
Brandon Soto Picado 