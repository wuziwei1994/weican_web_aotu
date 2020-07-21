# author:吴紫葳
# times:2020/7/21 11:59
# # coding:-*- utf-8 -*-

from pages.homePage import HomePage
import time
import unittest


class HomePageCase(unittest.TestCase):
    """测试首页类"""

    def test_home_choose(self):
        """
        逐个点击首页标签
        :return:
        """
        time.sleep(2)
        HomePage.get_order_box().click()
        HomePage.get_home_box().click()
        HomePage.get_chart_box().click()
        HomePage.get_market_box().click()
        HomePage.get_userElement_box().click()
        HomePage.get_settingElement_box().click()


if __name__ == '__main__':
    unittest.main()
