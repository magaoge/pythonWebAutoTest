from selenium.webdriver.common.by import By

class LoginElements:
    # 元素定位
    # 登录icon
    login_icon_class = (By.CLASS_NAME,"header-btn1")
    # 用户名输入框
    username_input_id = (By.ID,"username")
    # 密码输入框
    password_input_id = (By.ID,"password-o")
    # 登录按钮
    login_button_class = (By.CLASS_NAME,"loginBtn")

    # 登陆成功元素定位
    login_sesscuseText_Xpath = (By.XPATH,"//a[text() = '个人中心']")

    # 登陆失败元素定位
    login_fieldText_Xpath = (By.XPATH,"//em[text()='登录失败,请确认账号和密码正确']")
