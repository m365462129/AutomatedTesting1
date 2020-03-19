##----------------------------------------------------------基本配置
#配置浏览器驱动类型
driver_type = "chrome"
#配置运行的url
url = "https://www.baidu.com"
#设置失败重跑次数
rerun = 3
#运行测试用例的目录或者文件
cases_path = "./test_dir"


##----------------------------------------------------------浏览器驱动
import pytest
from selenium import webdriver
@pytest.fixture(scope="session",autouse=True)
def browser():
    """
    定义全局的浏览器驱动
    :return:
    """
    global driver
    global driver_type

    if driver_type == "chrome":
        driver = webdriver.Chrome()
    elif driver_type == "firefox":
        driver = webdriver.Firefox()
    elif driver_type == "chrome-headless":
        # driver = webdriver
        pass
    else:
        raise NameError("driver驱动类型定义错误")
    return driver

@pytest.fixture(scope="session",autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("---------------test end")


##----------------------------------------------------------失败截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    :Param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report  = outcome.get_result()
    


