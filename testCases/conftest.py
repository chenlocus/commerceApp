from selenium import webdriver
import pytest

@pytest.fixture(params=["chrome", "firefox"],scope="class")
def setup(request):
    #print("browser=",browser)
    # if browser=="chrome":
    #     driver = webdriver.Chrome()
    # elif browser =="firefox":
    #     driver = webdriver.Firefox()
    # return driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param =="firefox":
        driver = webdriver.Firefox()
    return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store",default="chrome")
#
#
# @pytest.fixture()
# def browser(request):
#     print("get browser type")
#     return request.config.getoption("--browser")
