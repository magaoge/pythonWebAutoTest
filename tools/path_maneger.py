# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 4:49 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : path_maneger.py
# @Software: PyCharm
import datetime
import os

# 返回当前文件相对路径
# os.path.split应该是以系统分隔符去切分获取到的路径
project_root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# os.path.join(path ,*paths),将path和后面所有的paths变量拼接为字符串路径返回

# 浏览器驱动路径
chrome_driver_path = os.path.join(project_root_path,"resource","chromedriver.exe")


test_data_path = os.path.join(project_root_path,"test_data","apiTestData.xlsx")

# 测试报告路径
test_report_path = os.path.join(project_root_path,"TestResult/html_report","test_repoet.html")

# 测试日志路径
day_time = datetime.datetime.now().strftime('%Y%m%d')
test_log_path = os.path.join(project_root_path,"TestResult/logs","test_log_"+day_time+".txt")

# 测试报错截图路径
screen_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
def get_screen_shot_path(doc):
    screen_shot_path = os.path.join(project_root_path, "TestResult/screen_shot", doc + "_" + screen_time + ".png")
    return screen_shot_path

# if __name__ == '__main__':
#     screen_shot_path = get_screen_shot_path("首页")
#     print(screen_shot_path)
#     print(day_time)