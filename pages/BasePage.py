from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Clase Padre de todas la paginas
contiene todos lo metodos genericos para las paginas."""

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeoutSec = 20

    def find(self,by_locator):
        return self.driver.find_element(by_locator[0],by_locator[1])
    
    def find_all_elements(self,by_locator):
        return self.driver.find_elements(by_locator[0],by_locator[1])

    def click(self, by_locator):
        self.find(by_locator).click()

    def clear(self, by_locator):
        self.find(by_locator).clear()

    def submit(self, by_locator):
        self.find(by_locator).submit()

    def text(self, by_locator):
        return self.find(by_locator).get_text()
    
    def type(self, by_locator, text: str):
        self.find(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeoutSec).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.timeoutSec).until(EC.visibility_of_element_located(by_locator))
        return bool(element)