import time

from ddt2 import ddt,data
from selenium import webdriver
import unittest
from PageObject.login_page import LoginPage
from TestData.login_test_data import *
from PageLocators.page_login import LoginElements as loc
from tools.mylog import MyLog
from PageObject.base_page import Basic
import pytest

@pytest.mark.smoke
def test_pytest():
    print("这个的标记是smoke")

@pytest.mark.usefixtures("access_web")
# pytest 的fixture功能和@ddt是不能共用的
@pytest.mark.usefixtures("refresh") # 作用与类中的所有函数之上
class TestLogin:

    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("refresh") # 可以标记在函数上，也可以标记在类上，作用于类中的所有函数
    # # access_web 是fixture修饰的函数名称，用来作为接受它返回值的参数名
    # def test_1_login_success(self,access_web):
    #     LoginPage(access_web).login("16621710374","magaoge..00")
    #     # 断言判断，三种方式，根据实际的场景来使用：
    #     # 1.find_element
    #     # 2.显式等待加载页面元素，加载不到·判断错误
    #     # 3.assert
    #     time.sleep(0.5)
    #     assert True
    #     # self.assert_by_txt("个人中心",loc.login_sesscuseText_Xpath,doc="首页_登录_登录成功断言")

    # # 将浏览器初始化的动作级别放在类前，注意是TestCase类的方法重写
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(r"C:\Users\MAG\PycharmProjects\pyWebAutoTest\resource\chromedriver.exe")
    #     cls.driver.maximize_window()
    #     cls.driver.get("https://www.juhe.cn/?bd_vid=10590455537289017250")
    #
    # # 将浏览器关闭的动作级别放在类执行后
    # @classmethod
    # def tearDownClass(cls):
    #     "Hook method for deconstructing the class fixture after running all tests in the class."
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     pass
    #
    # # 由于我们要在输入之后，重新写入数据，所以要每次用例执行完进行一次刷新的操作
    # def tearDown(self):
    #     # self.driver.refresh()
    #     # 由于这个页面刷新不起作用，我们重新进入页面
    #     self.driver.get("https://www.juhe.cn/?bd_vid=10590455537289017250")

    # 查看源码，可以看到parametrize底层本身接收的就是数组类型参数，所以不用*脱衣
    @pytest.mark.parametrize("data",login_erro_data)
    def test_0_login(self, data,access_web):
        print(data)
        LoginPage(access_web).login(data["phoneNum"], data["password"])
        # 断言判断，三种方式，根据实际的场景来使用：
        # 1.find_element
        # 2.显式等待加载页面元素，加载不到判断错误
        # 3.assert
        time.sleep(0.5)
        # assert True
        LoginPage(access_web).assert_by_txt(access_web,data["expect"],loc.login_fieldText_Xpath,doc="首页_登录_登录失败断言")

    @pytest.mark.parametrize("data",login_success_data)
    @pytest.mark.smoke
    def test_1_login_success(self,data,access_web):
        LoginPage(access_web).login(data["phoneNum"],data["password"])
        # 断言判断，三种方式，根据实际的场景来使用：
        # 1.find_element
        # 2.显式等待加载页面元素，加载不到判断错误
        # 3.assert
        time.sleep(0.5)
        # assert True
        LoginPage(access_web).assert_by_txt(access_web,data["expect"],loc.login_sesscuseText_Xpath,doc="首页_登录_登录成功断言")



    # # 根据断言元素文本的断言方法
    # def assert_by_txt(self,access_web,excepct,locator,doc=""):
    #     """
    #     :param excepct:预期的结果值
    #     :param locater: 希望对比的实际数据的元素定位坐标
    #     :param doc:
    #     :return:
    #     """
    #     MyLog.info("需要获取文本断言的元素是{}".format(locator))
    #     txt = LoginPage(access_web).get_element_text(locator,doc=doc)
    #     try:
    #         assert excepct == txt
    #         return True
    #     except:
    #         MyLog.exception("{}文本断言失败！".format(doc))
    #         Basic(access_web).my_save_screenshot(doc)
    #         return False
