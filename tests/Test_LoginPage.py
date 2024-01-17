from tests.TestBase import TestBase
from utils.TestData import TestData
from pages.LoginPage import LoginPage

class TestLogin(TestBase):

    def test_doLogin(self):
        self.login_Page = LoginPage(self.driver)
        self.login_Page.signIn(TestData.USERNAME, TestData.PASSWORD)
        assert self.login_Page.verifyLogin() == 'Inside ADManager Plus'