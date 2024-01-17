from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

class ManagementPage(BasePage):
    btn_lupa = (By.XPATH, "//li[@class='search-field']/i")
    input_search = (By.ID, "searchText")
    btn_close_search = (By.XPATH, "//li[@class='search-field']/span[@class='search-base']/i")
    headers = (By.XPATH, "//table[@id='resultList']/thead/tr")
    table_user = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[2]")
    table_name = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[3]")
    table_ouname = (By.XPATH, "//table[@id='resultList']/tbody/tr/td[4]")

    btn_reset = (By.XPATH, "//table[@id='resultList']//td[6]//a")

    def __init__(self, driver):
        super().__init__(driver)

    def do_click_lupa(self):
        self.click(self.btn_lupa)

    def do_click_close_textbox(self):
        self.click(self.btn_close_search)

    def do_click_reset(self):
        self.click(self.btn_reset)

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