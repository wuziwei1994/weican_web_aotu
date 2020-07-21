# author:吴紫葳
# times:2020/7/21 15:19
# # coding:-*- utf-8 -*-

from pages.orderPage import OrderPage
import time
import unittest


class OrderPageCase(unittest.TestCase):
    def test_order_left_page(self):
        time.sleep(2)
        OrderPage.to_page()
        time.sleep(3)
        for one in OrderPage.get_order_box():
            time.sleep(1)
            one.click()


