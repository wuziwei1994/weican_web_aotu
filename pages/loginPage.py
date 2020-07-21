# author：wuziwei   
# @time:2020-07-18 20:27
# coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage


class LoginPage(BasePage):
    """登录页面元素定位类"""

    def __init__(self):
        # 执行父类的构造方法
        super().__init__()
        # 登录账号、密码框，需根据 placeholder 的值去判断框
        self.inputBoxElements = (By.CSS_SELECTOR, 'input.login-input-full')
        # 验证码输入框
        self.codeBoxElement = (By.CSS_SELECTOR, 'input.login-input-code')
        # 登录按钮
        self.loginBottonElement = (By.CSS_SELECTOR, 'input.login-form-login')

    def gets_login_box(self):
        """定位各输入框元素"""
        return self.get_elements(self.inputBoxElements)

    def get_code_box(self):
        """定位验证码输入框元素"""
        return self.get_element(self.codeBoxElement)

    def get_login_botton(self):
        """定位登录元素"""
        return self.get_element(self.loginBottonElement)
