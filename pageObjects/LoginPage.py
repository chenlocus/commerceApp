from selenium import webdriver
from .BaseElement import BaseElement
from .BasePage import BasePage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig

class LoginPage(BasePage):
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"
    button_logout_xpath="//*[@id='navbarText']/ul/li/a[text()='Logout']"
    url = ReadConfig.getApplicationURL()

    @property
    def username_input(self):
        locator = (By.ID,self.textbox_username_id)
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
    @property
    def password_input(self):
        locator = (By.ID, self.textbox_password_id)
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def login_button(self):
        locator = (By.XPATH, self.button_login_xpath)
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def logout_button(self):
        locator = (By.XPATH, self.button_logout_xpath)
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])



