from selenium import webdriver
# 1.引入pytest
import pytest
from tools.path_maneger import *

driver = None

# 2.声明一个类级别的fixture
@pytest.fixture(scope="class")
def access_web():
    print("========类公用=========")
    global driver
    driver = webdriver.Chrome(chrome_driver_path)
    driver.maximize_window()
    driver.get("https://www.juhe.cn/?bd_vid=10590455537289017250")
    # yield作用1：分割前后置的行为；
    # 作用2：返回参数，返回多个参数时，返回的数据格式是自己定义的
    # 例：yield [driver1,driver2......]
    yield driver
    driver.quit()


# 3.声明一个函数级别的fixture
@pytest.fixture(scope="function")
def refresh():
    global driver
    print("========方法公用=========")
    yield
    driver.get("https://www.juhe.cn/?bd_vid=10590455537289017250")


def pytest_configure(config):
    marker_list = ["smoke"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
