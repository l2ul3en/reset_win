import time
from pages.LoginPage import LoginPage
from tests.TestBase import TestBase
from utils.TestData import TestData

class TestFlowReset(TestBase):
    
    def test_flow_reset_windows_password(self):
        
        self.loginpage.signIn(TestData.W_USER, TestData.W_PASS)
        self.homepage.do_click_reset_password_console()
        self.managementpage.do_click_lupa()
        self.managementpage.do_send_username("villartem")
        time.sleep(2)
        
        tname = self.managementpage.get_table_name()
        tuser = self.managementpage.get_table_user()
        touname = self.managementpage.get_table_ouname()
        
        print(type(tname),type(tuser), type(touname))
        if len(tname) == len(tuser) == len(touname):
            for i in range(len(tname)):
                if tuser[i].text.strip() == "villartem":
                    print(tname[i].text, tuser[i].text, touname[i].text)
        
        assert False == True
        