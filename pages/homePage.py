# author:吴紫葳
# times:2020/7/21 11:26
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage
from config.settings import URL


class HomePage(BasePage):
    """首页元素定位类"""

    def __init__(self, path='/home'):
        super(HomePage, self).__init__()
        # 访问首页，拼接
        self.path = URL + path
        # 首页元素
        self.homeElement = (By.CSS_SELECTOR, 'a[href="/home"]')
        # 订单元素
        self.orderElement = (By.CSS_SELECTOR, 'a[href="/order"]')
        # 报表元素
        self.chartElement = (By.CSS_SELECTOR, 'a[href="/chart"]')
        # 会员元素
        self.userElement = (By.CSS_SELECTOR, 'a[href="/user"]')
        # 营销元素
        self.marketElement = (By.CSS_SELECTOR, 'a[href="/market"]')
        # 设置元素
        self.settingElement = (By.CSS_SELECTOR, 'a[href="/setting"]')

    def to_page(self):
        """访问home页面"""
        self.driver.get(self.path)

    def get_home_box(self):
        """首页元素"""
        return self.get_element(self.homeElement)

    def get_order_box(self):
        """订单元素"""
        return self.get_element(self.orderElement)

    def get_chart_box(self):
        """报表元素"""
        return self.get_element(self.chartElement)

    def get_market_box(self):
        """营销元素"""
        return self.get_element(self.marketElement)

    def get_userElement_box(self):
        """会员元素"""
        return self.get_element(self.userElement)

    def get_settingElement_box(self):
        """设置元素"""
        return self.get_element(self.settingElement)


HomePage = HomePage()
