# author:吴紫葳
# times:2020/7/16 11:20
# # coding:-*- utf-8 -*-

from selenium import webdriver
from time import sleep


class LoginPage:
    ''' 登录元素类 '''

    def __init__(self):
        '''初始化driver对象'''
        self.driver = webdriver.Chrome(r'D:\weican_web_aotu\chromedriver.exe')
        self.driver.get('http://b.local.weicantimes.com/login')
        self.driver.maximize_window()
        self.merchant_id = '539848'
        self.account = 'wct'
        self.password = '123456'
        self.captcha = '123'

    def loginBox(self):
        ''' 获取登录所需元素 '''
        loginBox = self.driver.find_elements_by_css_selector('input.login-input-full')
        return loginBox

    def captchaBox(self):
        captchaBox = self.driver.find_element_by_css_selector('input.login-input-code')
        return captchaBox

    def loginButton(self):
        ''' 获取登录按钮 '''
        loginButton = self.driver.find_element_by_css_selector('input.login-form-login')
        return loginButton


class Login(LoginPage):
    ''' 进行登录 '''

    def login(self):
        for one in self.loginBox():
            if '请输入商家编号' in one.get_attribute('placeholder'):
                one.send_keys(self.merchant_id)
            elif '请输入账号' in one.get_attribute('placeholder'):
                one.send_keys(self.account)
            elif '请输入密码' in one.get_attribute('placeholder'):
                one.send_keys(self.password)
                break
        self.captchaBox().send_keys(self.captcha)
        self.loginButton().click()
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    Login().login()
