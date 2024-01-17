from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):
    input_user = (By.ID, 'j_username')
    input_password = (By.ID, 'j_password')
    btn_sign_in = (By.ID,"loginButton")
    verify_login = (By.TAG_NAME,"h1")

    def __init__(self,driver):
        super().__init__(driver)
        

    def signIn(self,user,password):
        self.type(self.input_user, user)
        self.type(self.input_password, password)
        self.click(self.btn_sign_in)

    def verifyLogin(self) -> str:
        message = self.get_element_text(self.verify_login)
        return message