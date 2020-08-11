# author:吴紫葳
# times:2020/7/21 15:19
# # coding:-*- utf-8 -*-

from pages.orderPage import OrderPage
import time
import pytest


class TestOrderPageCase:

    def test_all_order_page(self):
        time.sleep(1)
        OrderPage.to_all_order_page()

    def test_times_search(self):
        time.sleep(2)
        OrderPage.to_all_order_page()
        OrderPage.get_order_time_box().click()
        OrderPage.get_star_data_times().send_keys('2020-08-01')
        OrderPage.get_end_data_times().send_keys('2020-08-30')
        OrderPage.get_choose_data_ok_button_box().click()
        OrderPage.get_inquiry_button_box().click()
        assert '详情' == OrderPage.assert_search_result().text



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
