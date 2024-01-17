from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class HomePage(BasePage):
    btn_help_desk = (By.XPATH, "//div[@class='helpdesk-btn']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_click_reset_password_console(self):
        if self.is_visible(self.btn_help_desk):
            self.click(self.btn_help_desk)