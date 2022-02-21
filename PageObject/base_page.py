import os, inspect
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 作为练习赶进度,这里就不再集成日志机制,与接口自动化中的日志相同,后面再去处理
# import MyLog
import unittest
from tools.path_maneger import *
from tools.mylog import MyLog
import datetime

class Basic:

    def __init__(self,driver):
        self.driver = driver

    # 等待页面加载元素
    def wait_element_located(self,locator,timeout = 10,poll_frequency=0.5,doc=""):
        """
        :param doc : 模块名_页面名称_操作名称
        :param locator: 元组数据,其中是(元素定位方式,定位元素坐标)
        :param timeout: 超时时间,默认单位:秒
        :param poll_frequency: 每多久重试一次
        :return:
        """
        MyLog.info("等待加载的元素是:{}".format(locator))
        print("等待加载的元素是:{}".format(locator))
        try:
            startime = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            endtime = datetime.datetime.now()
            # 计算等待时长
            waitime = endtime - startime
            MyLog.info("加载时间为:{}".format(waitime))
        except:
            #将error级别信息,同时显示在控制台
            MyLog.exception("元素加载显示失败!")
            self.my_save_screenshot(doc)
            raise

    # 判断页面是否存在元素
    def wait_element_Presence(self,locator,timeout = 15,poll_frequency=0.5):
        MyLog.info("等待显示的元素是:{}".format(locator))
        try:
            startime = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(locator))
            endtime = datetime.datetime.now()
            # 计算等待时长
            waitime = endtime - startime
            MyLog.info("判断耗时时间为:{}".format(waitime))
        except:
            #将error级别信息,同时显示在控制台
            MyLog.exception("无法找到元素!元素不存在!")
            raise

    # 查找元素
    def get_element(self,locator,doc=""):
        MyLog.info("查找的元素是:{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            MyLog.exception("无法找到{}元素!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self,locator,doc=""):
        MyLog.info("点击的元素是:{}".format(locator))
        try:
            self.get_element(locator,doc).click()
        except:
            MyLog.exception("无法点击{}元素!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self,locator,key_content,doc=""):
        MyLog.info("输入的元素是:{}".format(locator))
        try:
            self.get_element(locator,doc).send_keys(key_content)
        except:
            MyLog.exception("无法输入{}元素!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self,locator,doc=""):
        MyLog.info("需要获取文本的元素是:{}".format(locator))
        try:
            return self.get_element(locator,doc).text()
        except:
            MyLog.exception("无法获取{}元素文本!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 获取元素的属性值
    def get_attribute(self,locator,attribute_name,doc=""):
        MyLog.info("需要获取文本的元素是:{}".format(locator))
        try:
            return self.get_element(locator, doc).get_attribute(attribute_name)
        except:
            MyLog.exception("无法获取{}元素文本!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # alter的处理
    def alter_action(self,choose,timeout = 15,poll_frequency=0.5,doc=""):

        MyLog.info("alter的选择是{}".format(choose))

        # 返回alter文本内容
        # return alter.text
        try:
            WebDriverWait(self.driver, timeout,poll_frequency).until(EC.alert_is_present())
            alter = self.driver.switch_to.alert
            if choose == "accept" :
                alter.accept()
            elif choose == "dismiss" :
                alter.dismiss()
            else:
                print("alter行为，无效的action值！")
        except:
            MyLog.exception("操作{}alter失败!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # iframe切换
    # 如果iframe中还有iframe，那就一层一层的跳进去（方法调用的时候控制传入数据的格式，利用循环就可以）
    def switch_iframe(self,action,locator,timeout = 15,poll_frequency=0.5,doc=""):
        """
        :param action:  根据action去指定不同的iframe行为,有效参数仅为"switch_in"，"back_parent"，"back_default"
        :param locator: 所在页面中声明iframe的元素信息，元组数据格式(定位方式，定位元素)
        :param timeout:
        :param poll_frequency:
        :return:
        """
        MyLog.info("需要{0}的iframe是:{1}".format(action,locator))

        try:
            if action == "switch_in" :
                # 无需返回值，调用函数之后，直接就进入iframe内
                iframe_locater = EC.frame_to_be_available_and_switch_to_it((locator))
                WebDriverWait(self.driver,timeout,poll_frequency).until(iframe_locater)
            elif action == "back_parent":
                # 返回上一层
                self.driver.switch_to.parent_frame()
            elif action == "back_default":
                # 从iframe页面中回到默认外层页面中
                self.driver.switch_to.default_content()
            else:
                print("iframe行为，无效的action值！")
        except:
            MyLog.exception("操作{}iframe失败!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 上传操作
    def upload_file(self,doc=""):
        # 遇到再说，之前也没有练习过

        try:
            MyLog.info("".format())
        except:
            MyLog.exception("操作{}scroll_bar失败!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 滚动指定元素与浏览器窗口底部对齐
    def scroll_bar(self,locator,doc=""):
        MyLog.info("需要滚动条滚动的元素是{0}".format(locator))
        try:
            self.wait_element_located(locator,doc = doc)
            element = self.get_element(locator,doc)
            self.driver.execute_script("arguments[0].scrollIntoView(false);",element)
        except:
            MyLog.exception("操作{}scroll_bar失败!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 窗口切换
    def change_window(self,index,doc=""):
        """
        :param index: 用于操作获取到的句柄列表的索引，从0开始
        :param doc:
        :return:
        """
        # # 打开新的窗口
        # # 判断新的窗口是否出现,本质是判断handles有没有变化
        # is_open_new_window = EC.new_window_is_opened(handles)
        # WebDriverWait(driver, 10).until(is_open_new_window)
        try:
            # 获取当前对话浏览器的所有窗口句柄，句柄获取的顺序取决于窗口打开的顺序
            handles = self.driver.window_handles
            MyLog.info("当前所有的窗口句柄信息是{}".format(handles))
            # 获取当前所在窗口句柄
            MyLog.info("当前所在的窗口句柄是{}".format(self.driver.current_window_handle))
            # 切换窗口，根据索引切换至指定窗口中
            self.driver.switch_to.window(handles[index])
            # 获取当前所在窗口句柄
            MyLog.info("当前所在切换后的窗口句柄是{}".format(self.driver.current_window_handle))
        except:
            MyLog.exception("操作{}切换窗口失败!".format(doc))
            self.my_save_screenshot(doc)
            raise

    # 截图操作
    def my_save_screenshot(self,doc=""):
        # 图片名称:模块名_页面名称_操作名称_time.png

        file_name = get_screen_shot_path(doc)

        MyLog.info("图片保存路径是=========={}".format(file_name))
        try:
            self.driver.save_screenshot(file_name)
            MyLog.info("图片保存成功,存储位置在{}".format(file_name))
        except:
            MyLog.info("{}模块图片保存失败!!!".format(doc))
            raise

# screenshot方法重写的思路，但是因为我们已经声明了这个路径，所以就不再使用这个重写方式，但是思想值得学习
# def screenshot(driver,file_path = None):
#     #用户没有传参数
#     if  file_path == None:
#         project_path = os.path.dirname(os.getcwd())
#         print(project_path)
#         file_path = project_path +"/images/"
#         if not os.path.exists(file_path):
#             os.mkdir(file_path)
#         images_name = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#         file_path = file_path+images_name+".png"
#         print(file_path)
#     driver.save_screenshot(file_path)

    # 获取元素文本的方法
    def get_element_text(self,locator,doc=""):
        MyLog.info("需要获取文本断言的元素是{}".format(locator))
        try:
            self.wait_element_located(locator,doc=doc)
            # 获取元素文本的text函数调用不要括号，括号针对link
            txt = self.get_element(locator,doc).text
            return txt
        except:
            MyLog.exception("{}获取文本失败！".format(doc))
            Basic(self.driver).my_save_screenshot(doc)
            raise

    # 通过页面是否存在该元素进行断言
    def judgement_is_element_load(self,locator,doc=""):
        MyLog.info("需要等待加载的元素是{}".format(locator))
        try:
            self.wait_element_located(locator, doc=doc)
            return True
        except:
            MyLog.exception("{}页面的{}元素失败！".format(doc,locator))
            Basic(self.driver).my_save_screenshot(doc)
            return False

    # 根据断言元素文本的断言方法
    def assert_by_txt(self,access_web,excepct,locator,doc=""):
        """
        :param excepct:预期的结果值
        :param locater: 希望对比的实际数据的元素定位坐标
        :param doc:
        :return:
        """
        MyLog.info("需要获取文本断言的元素是{}".format(locator))
        txt = self.get_element_text(locator,doc=doc)
        try:
            assert excepct == txt
        except:
            MyLog.exception("{}文本断言失败！".format(doc))
            Basic(access_web).my_save_screenshot(doc)
            raise