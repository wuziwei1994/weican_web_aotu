# author:吴紫葳
# times:2020/7/21 11:59
# # coding:-*- utf-8 -*-

from pages.homePage import HomePage
import time
import pytest


class TestHomePageCase:
    """测试首页类"""

    def test_title_home(self):
        """测试逐个点击首页标签"""
        time.sleep(2)
        # 点击订单页面
        HomePage.get_order_box().click()
        assert '全部订单' in HomePage.get_all_order_box().text

        # 点击首页
        HomePage.get_home_box().click()
        assert '本月营业金额' in HomePage.get_home_check_box().text

        # 点击报表页面
        HomePage.get_chart_box().click()
        assert '门店报表' in HomePage.get_store_report_box().text

        # 点击营销页面
        HomePage.get_market_box().click()
        assert '营销方案' in HomePage.get_market_plan_box().text

        # 点击会员页面
        HomePage.get_user_box().click()
        assert '会员管理' in HomePage.get_user_manage_box().text

        # 点击设置页面
        HomePage.get_setting_box().click()
        assert '门店设置' in HomePage.get_store_settings().text


if __name__ == '__main__':
    pytest.main()
