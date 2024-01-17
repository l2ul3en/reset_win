import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ManagementPage import ManagementPage

from utils.TestData import TestData

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        # Inicializar el WebDriver de Chrome
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    if request.param == "firefox":
        # Inicializar el WebDriver de Firefox
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    #Maximizar la ventana y abrir url
    web_driver.maximize_window()
    web_driver.get(TestData.URL)
    
    # Establecer el atributos en la instancia de la clase de prueba
    request.cls.driver = web_driver
    request.cls.loginpage = LoginPage(web_driver)
    request.cls.homepage = HomePage(web_driver)
    request.cls.managementpage = ManagementPage(web_driver)
    yield #Devuelve el control a las pruebas
    
    #Cerra el navegador luego que las pruebas se ejecutaron
    web_driver.close()