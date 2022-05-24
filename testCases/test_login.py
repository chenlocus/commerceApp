import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    print("logger=",logger)

    def test_homePageTitle(self,setup):
        self.logger.info('************Test_001_Login **************')
        self.logger.info('************verify home page title **************')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.go()
        act_title = self.lp.title
        self.lp.quit()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("************Test_001_Login passed **************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetile.png")
            assert False
            self.logger.info("************Test_001_Login failed **************")

    def test_login(self,setup):
        self.logger.info("************Test_001_Login verify login page**************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.go()
        self.lp.username_input.input_text(self.username)
        self.lp.password_input.input_text(self.password)
        self.lp.login_button.click()
        act_title = self.lp.title
        self.lp.quit()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************Test_001_Login verify login page passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.logger.info("************Test_001_Login verify login page failed**************")

