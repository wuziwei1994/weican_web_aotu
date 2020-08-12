# author:吴紫葳
# times:2020/8/12 10:28
# # coding:-*- utf-8 -*-

from pages.orderPage import OrderPage


class OrderPublic:
    @classmethod
    def public_send_times_search(cls, star_time, end_time):
        """订单页面，输入日期方法"""
        OrderPage.get_order_time_box().click()
        OrderPage.get_star_data_times().send_keys(star_time)
        OrderPage.get_end_data_times().send_keys(end_time)
        OrderPage.get_choose_data_ok_button_box().click()


OrderPublic = OrderPublic()
