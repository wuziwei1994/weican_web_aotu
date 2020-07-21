# author：wuziwei   
# @time:2020-07-18 20:08
# coding:-*- utf-8 -*-

from selenium import webdriver
from config.settings import DRIVERPATH, URL, MERCHANT_ID, ACCOUNT, PASSWORD
from time import sleep


class Driver:
    """浏览器驱动类"""
    # 初始化driver对象为空
    driver = None

    @classmethod
    def get_driver(cls, browser_name='Chrome'):
        """
        获取浏览器对象，最大化浏览器并访问默认网页获取浏览器对象，最大化浏览器并访问默认网页
        :param browser_name: 默认为 Chrome，可填写浏览器类型
        :return:
        """
        # 创建driver浏览器方法
        if cls.driver is None:
            if browser_name == 'Chrome':
                cls.driver = webdriver.Chrome(DRIVERPATH['Chrome'])
            elif browser_name == 'Firefox':
                cls.driver = webdriver.Firefox(DRIVERPATH['Firefox'])
            elif browser_name == 'Ie':
                cls.driver = webdriver.Ie(DRIVERPATH['Ie'])

            # 浏览器最大化
            cls.driver.maximize_window()
            # 访问默认网址
            cls.driver.get(URL)
            # 强制等待1秒自动跳转页面
            sleep(1)
            # 执行登录
            cls.__login()

        return cls.driver

    @classmethod
    def __login(cls):
        """登录方法"""
        cls.driver.find_element_by_css_selector('input[placeholder="请输入商家编号"]').send_keys(MERCHANT_ID)
        cls.driver.find_element_by_css_selector('input[placeholder="请输入账号"]').send_keys(ACCOUNT)
        cls.driver.find_element_by_css_selector('input[placeholder="请输入密码"]').send_keys(PASSWORD)
        cls.driver.find_element_by_css_selector('input[placeholder="请输入验证码"]').send_keys('123')
        cls.driver.find_element_by_css_selector('input.login-form-login').click()


if __name__ == '__main__':
    Driver.get_driver()
