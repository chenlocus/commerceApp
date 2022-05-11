from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
