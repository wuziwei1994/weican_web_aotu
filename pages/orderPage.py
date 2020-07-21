# author:吴紫葳
# times:2020/7/21 15:03
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage
from config.settings import URL


class OrderPage(BasePage):
    """订单页面类"""

    def __init__(self):

        super(OrderPage, self).__init__()
        # 订单左侧全部订单
        self.allOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/all"]')
        # 订单左侧未支付订单
        self.noPayOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/nopay"]')
        # 订单左侧已支付订单
        self.paidOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/paied"]')
        # 订单左侧退款订单
        self.refundOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/refund"]')
        # 订单左侧反结账订单
        self.recheckoutOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/recheckout"]')
        # 订单左侧已取消订单
        self.cancelOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/cancel"]')

    def get_order_box(self):
        return self.get_elements(self.orderElement)

OrderPage = OrderPage()

