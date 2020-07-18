# author：wuziwei   
# @time:2020-07-18 20:22
# coding:-*- utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.driver import Driver
from lib.settings import TIMEOUT, POLL_FREQUENCY


class BasePage:
    def __init__(self):
        # 构造driver对象
        self.driver = Driver.get_driver()

    def get_element(self, locator):
        '''
        显示等待，并返回元素对象，超时时间默认5秒，轮训时间默认0.5秒
        Args:
            locator: 传入元祖，0位表示元素定位方法，1位表示元素表达式
        Returns:

        '''
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 返回元素对象
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        '''
        显示等待，并返回元素列表，超时时间默认5秒，轮训时间默认0.5秒
        Args:
            locator: 传入元祖，0位表示元素定位方法，1位表示元素表达式

        Returns:

        '''
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 返回元素列表
        return self.driver.find_elements(*locator)
