import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/loginData.xlsx"
    logger = LogGen.loggen()
    print("logger=",logger)

    def test_login_ddt(self,setup):
        self.logger.info("************Test_001_Login verify login page**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')

        lst_status = []
        for r in range(2, self.rows+1):
            self.user = ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            self.driver.close()
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************ pass**************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                else:
                    self.logger.info("************fail**************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("************fail**************")
                    lst_status.append("Fail")
                else:
                    self.logger.info("************pass**************")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("************Test_002_DDT_Login pass**************")
                assert True
            else:
                self.logger.info("************Test_002_DDT_Login fail**************")
                assert False
        self.logger.info("************End of Test_002_DDT_Login**************")