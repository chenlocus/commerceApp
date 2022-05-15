import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("********************Test_003_AddCustomer**************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********************Login successful**************************")
        self.logger.info("********************start Test_003_AddCustomer**************************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)
        self.addcust.clickOnAddnew()
        self.logger.info("********************provide customer info**************************")
        self.email = self.random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Howard")
        self.addcust.setLastName("Chan")
        self.addcust.setDob("8/05/1980")
        self.addcust.setCompanyName("cboe")
        self.addcust.setAdminContent("for test purpose")
        self.addcust.clickOnSave()
        self.logger.info("********************add customer info complete**************************")

        self.logger.info("********************validate customer info**************************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        self.driver.close()
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********************add customer info passed**************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("********************add customer info failed**************************")
            assert False

    def random_generator(self):
        size = 8
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

