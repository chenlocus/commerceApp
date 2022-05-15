from selenium import webdriver
import pytest

@pytest.fixture(params=["chrome","firefox"],scope="class")
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

def pytest_configure(config):
    config._metadata['Project Name'] = "Commerce"
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hchen'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("java_home",None)
    metadata.pop('plugins',None)