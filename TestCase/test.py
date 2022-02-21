from PageObject.base_page import Basic
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMyMethod():

    driver = webdriver.Chrome(r"C:\Users\MAG\PycharmProjects\pyWebAutoTest\resource\chromedriver.exe")
    driver.maximize_window()
    driver.get("file:///C:/Users/MAG/OneDrive%20-%20Reed%20Elsevier%20Group%20ICO%20Reed%20Elsevier%20Inc/Desktop/test_web/tiaozhuan.html")

    locator = (By.XPATH, "/html/body/a")
    driver.find_element(*locator).click()
    Basic(driver).change_window(1)
    driver.find_element(*(By.XPATH, "/html/body/a")).click()
    Basic(driver).change_window(0)
    time.sleep(2)


    # Basic(driver).alter_action("accept")


    # locator2 = (By.ID, "su")
    # driver.find_element(*locator2).click()



    # locator = (By.NAME, "iframe_top")
    # Basic(driver).switch_iframe("switch_in",locator, timeout=15, poll_frequency=0.5, doc="")
    # locator2 = (By.XPATH, "/ html / body / header / div / div[2] / div[2] / a")
    # driver.find_element(*locator2).click()
    # time.sleep(3)
    # ele =  driver.find_element_by_xpath("//a[text()='用户反馈']")
    # print(ele,type(ele))
    # driver.execute_script("arguments[0].scrollIntoView(false);", ele)

    # locator3 = (By.XPATH, "//a[text()='用户反馈']")
    # Basic(driver).scroll_bar(locator3)
    time.sleep(2)

    # 关闭当前窗口
    # driver.close()
    # 退出浏览器
    driver.quit()
