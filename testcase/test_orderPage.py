# author:吴紫葳
# times:2020/7/21 15:19
# # coding:-*- utf-8 -*-

from pages.orderPage import OrderPage
from public.orderPublic import OrderPublic
import time
import pytest


class TestOrderPageCase:

    def test_all_order_page(self):
        """测试：进入全部订单页面"""
        time.sleep(1)
        OrderPage.to_all_order_page()

    def test_times_search(self):
        """测试：全部订单-根据下单时间搜索"""
        OrderPublic.public_send_times_search('2020-08-01', '2020-08-31')
        OrderPage.get_inquiry_button_box().click()
        assert '详情' == OrderPage.get_order_detail_box().text

    def test_all_order_num_search(self):
        """测试：全部订单--订单号+下单时间搜索"""
        OrderPage.get_input_order_num_box().send_keys('2008050001')
        OrderPage.get_inquiry_button_box().click()
        assert '2008050001' == OrderPage.get_order_num_box().text

    def test_all_order_desk_search(self):
        """测试：全部订单-餐桌/取餐号+下单时间搜索"""
        OrderPage.get_input_order_num_box().clear()
        OrderPage.get_desk_id_box().send_keys('大厅A区scan')
        OrderPage.get_inquiry_button_box().click()
        assert '大厅A区scan' == OrderPage.get_desk_id_num().text

    def test_all_order_

    def test_no_pay_order_page(self):
        time.sleep(1)
        OrderPage.to_no_pay_order_page()

    def test_paid_order_page(self):
        time.sleep(1)
        OrderPage.to_paid_order_page()

    def test_re_fund_order_page(self):
        time.sleep(1)
        OrderPage.to_re_fund_order_page()

    def test_re_checkout_order_page(self):
        time.sleep(1)
        OrderPage.to_re_checkout_order_page()

    def test_cancel_order_page(self):
        time.sleep(1)
        OrderPage.to_cancel_order_page()


if __name__ == '__main__':
    pytest.main()
