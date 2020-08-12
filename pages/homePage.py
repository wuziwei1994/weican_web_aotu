# author:吴紫葳
# times:2020/7/21 11:26
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage


class HomePage(BasePage):
    """首页元素定位类"""

    def __init__(self):
        super(HomePage, self).__init__()
        # 门店名称元素
        self.storeNameElement = (By.CSS_SELECTOR, '.top-location')
        # 门店列表元素
        self.storeListElements = (By.CSS_SELECTOR, '.top-shop-dialog-list')
        # 切换门店元素
        self.switchStoreElements = (By.CSS_SELECTOR, 'button.el-button--success')



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
        # 首页-检查元素
        self.homeCheckElement = (By.CSS_SELECTOR, '.home-main-body-block1-item .home-main-body-block1-item-span')
        # 订单-全部订单元素
        self.allOrderElement = (By.CSS_SELECTOR, '.left-nav-list-item-childs [aria-current="page"]')
        # 报表-门店报表元素
        self.storeReportElement = (By.CSS_SELECTOR, '.left-nav-list-item .left-nav-list-item-header')
        # 会员-会员管理
        self.userManageElement = (By.CSS_SELECTOR, '.left-nav-list-item-header')
        # 营销-营销方案元素
        self.marketPlanElement = (By.CSS_SELECTOR, '.left-nav-list-item span')
        # 设置-门店设置
        self.storeSettingsElement = (By.CSS_SELECTOR, '.left-nav-list-item-header')

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

    def get_user_box(self):
        """会员元素"""
        return self.get_element(self.userElement)

    def get_setting_box(self):
        """设置元素"""
        return self.get_element(self.settingElement)

    def get_home_check_box(self):
        """首页-检查断言元素"""
        return self.get_element(self.homeCheckElement)

    def get_all_order_box(self):
        """订单-全部订单元素"""
        return self.get_element(self.allOrderElement)

    def get_store_report_box(self):
        """报表-门店报表"""
        return self.get_element(self.storeReportElement)

    def get_user_manage_box(self):
        """会员-会员管理"""
        return self.get_element(self.userManageElement)

    def get_market_plan_box(self):
        """营销-营销方案"""
        return self.get_element(self.marketPlanElement)

    def get_store_settings(self):
        """设置-门店设置"""
        return self.get_element(self.storeSettingsElement)


HomePage = HomePage()
