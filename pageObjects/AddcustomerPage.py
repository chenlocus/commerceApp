import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen

class AddCustomer:
    lnkCustomers_menu_xpath ="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//li[@class='nav-item']//p[text()=' Customers']"
    btnAddnew_xpath = "//a[starts-with(@class, 'btn btn-primary')]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath ="//input[@id='Password']"
    txtcustomerRoles_xpath = "//Select[@id='SelectedCustomerRoleIds']"
    lstitemAdministrators_xpath = "//Select[@id='SelectedCustomerRoleIds']//option[text()='Administrator']"
    lstitemRegistered_xpath = "//Select[@id='SelectedCustomerRoleIds']//option[text()='Registered']"
    lstDeleteRegister_xpath ="//span[contains(text(),'Registered')]/following-sibling::span[@title='delete']"
    lstitemGuests_xpath = "//Select[@id='SelectedCustomerRoleIds']//option[text()='Guests']"
    lstitemVendors_xpath = "//Select[@id='SelectedCustomerRoleIds']//option[text()='Vendors']"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    idMaleGender_id = "Gender_Male"
    idFemaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    logger = LogGen.loggen()


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        element = self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        element = self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)
        print("role=------",role)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH,self.lstDeleteRegister_xpath).click()
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
            try:
                self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
            finally:
                self.driver.quit()
        elif role == "Vendors":
            self.logger.info("go to vendors branch************************************")
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
            self.logger.info("Vendor element is***************************************:%s",self.listitem)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        self.logger.info("self.listitem is***************************************:%s", self.listitem)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)


    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.idMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.idFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.idMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()











