# author:吴紫葳
# times:2020/7/21 18:46
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage
from config.settings import URL


class AllOrderPage(BasePage):
    """全部订单页面类"""

    def __init__(self, path='/order/shop/all'):
        super(AllOrderPage, self).__init__()
        # 拼接全部订单页面
        self.path = URL + path
        # 输入订单号元素
        self.inputOrderNumElement = (By.CSS_SELECTOR, 'input[placeholder="输入订单号"]')
        # 搜索下单时间，开始时间元素
        self.startOrderTimeElement = (By.CSS_SELECTOR, 'input.el-range-input:nth-child(2)')
        # 搜索下单时间，结束时间元素
        self.endOrderTimeElement = (By.CSS_SELECTOR, 'input.el-range-input:nth-child(4)')
        # 输入餐桌号/取餐号元素
        self.deskIdElement = (By.CSS_SELECTOR, 'input[placeholder="输入桌号、取餐号"]')
        # 筛选订单状态元素
        self.chooseOrderStatusElement = (By.CSS_SELECTOR, 'input[placeholder="筛选订单状态"]')
        # 输入最小订单金额
        self.minOrderMoneyElement = (By.CSS_SELECTOR, '.order-filters-main-money-d1>.el-input')
        # 输入最大订单金额
        self.maxOrderMoneyElement = (By.CSS_SELECTOR, '.order-filters-main-money-d2>.el-input')
        # 选择支付方式
        self.choosePayByElement = (By.CSS_SELECTOR, 'input[placeholder="筛选支付方式"]')
        # 查询按钮
        self.inquiryBottonElement = (By.CLASS_NAME, 'el-button el-button--success')
        # 重置按钮
        self.resetBottonElement = (By.CLASS_NAME, 'el-button el-button--default is-plain')
        # 选择页数
        self.chooseTabElement = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')

    def to_page(self):
        """访问全部订单页面"""
        self.driver.get(self.path)

    def get_inputOrderNumElement(self):
        pass



