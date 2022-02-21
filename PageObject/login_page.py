import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.page_login import LoginElements as loc
from PageObject.base_page import Basic


class LoginPage(Basic):
    # 登录
    def login(self,phoneNum,password):
        self.wait_element_located(loc.login_icon_class,doc="首页_登录_登录icon")
        self.click_element(loc.login_icon_class,doc="首页_登录_登录icon")
        self.input_text(loc.username_input_id,phoneNum, doc="首页_登录_输入账户名")
        self.input_text(loc.password_input_id,password, doc="首页_登录_输入密码")
        time.sleep(0.5)
        self.click_element(loc.login_button_class, doc="首页_登录_登录按钮")


        # 显式等待WebDriverWait(驱动,超时时间,轮询间隔时间默认0.5s).until(等待条件)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.login_icon_class))
        # 登录的一系列操作，*脱衣，脱掉元组的括号
        # self.driver.find_element(*loc.login_icon_class).click()
        # self.driver.find_element(*loc.username_input_id).send_keys(phoneNum)
        # self.driver.find_element(*loc.password_input_id).send_keys(password)
        # time.sleep(0.5)
        # self.driver.find_element(*loc.login_button_class).click()
