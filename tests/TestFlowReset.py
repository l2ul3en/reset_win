import time
#from pages.LoginPage import LoginPage
from tests.TestBase import TestBase
from utils.TestData import TestData

class TestFlowReset(TestBase):
    
    def test_flow_reset_windows_password(self, user='villartem', clave='12345'):
        self.loginpage.signIn(TestData.W_USER, TestData.W_PASS)
        self.homepage.do_click_reset_password_console()
        self.managementpage.do_click_lupa()
        self.managementpage.do_send_username(user)
        time.sleep(2)
        
        tname = self.managementpage.get_table_name()
        tuser = self.managementpage.get_table_user()
        touname = self.managementpage.get_table_ouname()
        
        print(type(tname),type(tuser), type(touname))
        if len(tname) == len(tuser) == len(touname):
            for i in range(len(tname)):
                if tuser[i].text.strip() == user:
                    print(tname[i].text, tuser[i].text, touname[i].text)
                    self.managementpage.do_click_apply_reset(int(i+1))
                    time.sleep(2)
                    self.driver.save_screenshot('./screenshot/img-tst1.png')
                    self.managementpage.do_change_password(clave)
                    time.sleep(2)
                    self.driver.save_screenshot('./screenshot/img-tst3.png')
                    assert TestData.CHANGE_SUCCESS not in self.managementpage.get_text_error(int(i+1))
        else:
            assert False, "la cantidad de elementos no es la misma"
        
        self.managementpage.do_logout()