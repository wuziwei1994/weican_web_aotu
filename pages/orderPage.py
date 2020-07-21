# author:吴紫葳
# times:2020/7/21 15:03
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage
from config.settings import URL


class OrderPage(BasePage):
    """订单页面类"""

    def __init__(self, path='/order/shop/all'):

        super(OrderPage, self).__init__()
        # 访问全部订单，拼接
        self.path = URL + path
        # 订单左侧元素列表
        self.orderElement = (By.CSS_SELECTOR, 'li.left-nav-list-item-childs-item')

    def to_page(self):
        self.driver.get(self.path)

    def get_order_box(self):
        return self.get_elements(self.orderElement)

OrderPage = OrderPage()

