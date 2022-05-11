import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    print("logger=",logger)

    def test_homePageTitle(self,setup):
        self.logger.info('************Test_001_Login **************')
        self.logger.info('************verify home page title **************')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
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
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************Test_001_Login verify login page passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.logger.info("************Test_001_Login verify login page failed**************")

