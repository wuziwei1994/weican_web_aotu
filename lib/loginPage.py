# author：wuziwei   
# @time:2020-07-18 20:27
# coding:-*- utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By
from lib.basePage import BasePage
from lib.settings import MERCHANT_ID, ACCOUNT, PASSWORD


class LoginPage(BasePage):
    """登录页面表达式类"""

    def __init__(self):
        # 执行父类的构造方法
        super().__init__()
        # 登录账号、密码框，需根据 placeholder 的值去判断框
        self.inputBox = (By.CSS_SELECTOR, 'input.login-input-full')
        # 验证码输入框
        self.codeBox = (By.CSS_SELECTOR, 'input.login-input-code')
        # 登录按钮
        self.loginBotton = (By.CSS_SELECTOR, 'input.login-form-login')

    def login_box(self):
        """定位各输入框元素"""
        return self.get_elements(self.inputBox)

    def code_box(self):
        """定位验证码输入框元素"""
        return self.get_element(self.codeBox)

    def login_botton(self):
        """定位登录元素"""
        return self.get_element(self.loginBotton)


class Login(LoginPage):
    """登录类，继承登录页面表达式"""

    def login(self):
        for one in self.login_box():
            if '请输入商家编号' in one.get_attribute('placeholder'):
                one.send_keys(MERCHANT_ID)
            elif '请输入账号' in one.get_attribute('placeholder'):
                one.send_keys(ACCOUNT)
            elif '请输入密码' in one.get_attribute('placeholder'):
                one.send_keys(PASSWORD)
                break
        self.code_box().send_keys('123')
        self.login_botton().click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    Login().login()
