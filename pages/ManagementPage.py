from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time

class ManagementPage(BasePage):
    btn_lupa = (By.XPATH, "//li[@class='search-field']/i")
    input_search = (By.ID, "searchText")
    btn_close_search = (By.XPATH, "//li[@class='search-field']/span[@class='search-base']/i")
    headers = (By.XPATH, "//table[@id='resultList']/thead/tr")
    table_user = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[2]")
    table_name = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[3]")
    table_ouname = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[4]")
    input_reset_pass = (By.ID, "password")
    input_reset_confirm_pass = (By.ID, "confirmPassword")
    checkbox_reset_nextlogon = (By.XPATH, "//label[@class='checkbox-inline']//input")
    select_checkbox_reset_nextlogon = (By.XPATH, "//label[@class='checkbox-inline']//ins")
    btn_reset_save = (By.ID, "save")
    #btn_reset = (By.XPATH, "//table[@id='resultList']//td[6]//a")

    def __init__(self, driver):
        super().__init__(driver)

    def do_click_lupa(self):
        self.click(self.btn_lupa)

    def do_click_close_textbox(self):
        self.click(self.btn_close_search)

    def do_click_apply_reset(self,pos: int):
        btn_reset = (By.XPATH, f"//table[@id='resultList']//tr[{pos}]/td[6]//a")
        self.click(btn_reset)

    def get_table_name(self):
        if self.is_visible(self.table_name):
            return self.find_all_elements(self.table_name)
    
    def get_table_user(self):
        if self.is_visible(self.table_user):
            return self.find_all_elements(self.table_user)
        
    def get_table_ouname(self):
        if self.is_visible(self.table_ouname):
            return self.find_all_elements(self.table_ouname)

    def get_headers(self):
        if self.is_visible(self.headers):
            return self.find_all_elements(self.headers)

    def do_send_username(self, username):
        self.type(self.input_search, username)
        self.type(self.input_search, Keys.RETURN)

    def do_change_password(self,password):
        self.type(self.input_reset_pass, password)
        self.type(self.input_reset_confirm_pass, password)
        check_box = self.find(self.checkbox_reset_nextlogon)
        text_box = self.find(self.select_checkbox_reset_nextlogon)
        if check_box.is_selected():
            text_box.click()
            self.driver.save_screenshot('./screenshot/img-tst2.png')
        self.click(self.btn_reset_save)

    def get_text_successfull(self,pos: int):
        msg = (By.XPATH, f"//table[@id='resultList']//tr[{pos}]/td[6]//table[@class='statusmsgtable']//td[contains(text(),'Successfully')]")
        return self.get_element_text(msg)
    
    def get_text_error(self,pos: int):
        msg = (By.XPATH, f"//table[@id='resultList']//tr[{pos}]/td[6]//table[@class='statusmsgtable']//td[contains(text(),'Error')]")
        return self.get_element_text(msg)