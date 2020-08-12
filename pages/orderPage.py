# author:吴紫葳
# times:2020/7/21 15:03
# # coding:-*- utf-8 -*-

from selenium.webdriver.common.by import By
from public.basePage import BasePage
from config.settings import HOST


class OrderPage(BasePage):
    """订单页面类"""

    def __init__(self, ):
        super(OrderPage, self).__init__()
        # 拼接全部订单页面
        self.allOrderPath = HOST + '/order/shop/all'
        # 拼接未支付订单页面
        self.noPayOrderPath = f'{HOST}/order/shop/nopay'
        # 拼接已支付订单页面
        self.paidOrderPath = f'{HOST}/order/shop/paied'
        # 拼接退款订单页面
        self.refundOrderPath = f'{HOST}/order/shop/refund'
        # 拼接反结账订单页面
        self.reCheckoutOrderPath = f'{HOST}/order/shop/recheckout'
        # 拼接已取消订单
        self.cancelOrderPath = f'{HOST}/order/shop/cancel'
        # 订单左侧全部订单
        self.allOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/all"]')
        # 订单左侧未支付订单
        self.noPayOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/nopay"]')
        # 订单左侧已支付订单
        self.paidOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/paied"]')
        # 订单左侧退款订单
        self.refundOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/refund"]')
        # 订单左侧反结账订单
        self.reCheckoutOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/recheckout"]')
        # 订单左侧已取消订单
        self.cancelOrderElement = (By.CSS_SELECTOR, 'a[href="/order/shop/cancel"]')
        # 输入订单号元素
        self.inputOrderNumElement = (By.CSS_SELECTOR, 'input[placeholder="输入订单号"]')
        # 搜索下单时间元素
        self.orderTimeElement = (By.CSS_SELECTOR, '.el-date-editor--datetimerange')
        # 选择日期中开始时间(日期)
        self.starDateTimesElement = (By.CSS_SELECTOR, '[placeholder="开始日期"]')
        # 选择日期中开始时间(小时/分)
        self.starTimesElement = (By.CSS_SELECTOR, '[placeholder="开始时间"]')
        # 选择日期中结束时间（日期）
        self.endDateTimesElement = (By.CSS_SELECTOR, '[placeholder="结束日期"]')
        # 选择日期中结束时间(小时/分)
        self.endTimesElement = (By.CSS_SELECTOR, '[placeholder="结束时间"]')
        # 选择日期中的确定按钮
        self.chooseDataOkBottonElement = (By.CSS_SELECTOR, '.el-picker-panel__footer>button.is-plain')
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
        self.inquiryButtonElement = (By.CSS_SELECTOR, 'button.el-button.el-button--success')
        # 重置按钮
        self.resetButtonElement = (By.CSS_SELECTOR, '.order-filters-main-btns button.el-button--default')
        # 选择页数
        self.chooseTabElement = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
        # 订单-全部订单-搜索出来结果中的详情元素
        self.orderDetailElement = (By.CSS_SELECTOR, 'a.el-button--text')
        # 订单-全部订单-搜索出来结果中的订单号
        self.orderNumElement = (By.CSS_SELECTOR, '.el-table__row>.orderall-main-body-contents-table-td-number>.cell')
        # 订单-全部订单-搜索出来结果中的餐桌号/取餐号
        self.deskIdNum = (By.CSS_SELECTOR, '.el-table__row>.orderall-main-body-contents-table-tdcell>.cell')

    def to_all_order_page(self):
        """进入全部订单页面"""
        return self.driver.get(self.allOrderPath)

    def to_no_pay_order_page(self):
        """进入未支付订单页面"""
        return self.driver.get(self.noPayOrderPath)

    def to_paid_order_page(self):
        """进入已支付订单页面"""
        return self.driver.get(self.paidOrderPath)

    def to_re_fund_order_page(self):
        """进入退款订单页面"""
        return self.driver.get(self.refundOrderPath)

    def to_re_checkout_order_page(self):
        """进入反结账订单页面"""
        return self.driver.get(self.reCheckoutOrderPath)

    def to_cancel_order_page(self):
        """进入已取消订单页面"""
        return self.driver.get(self.cancelOrderPath)

    def get_order_time_box(self):
        """获取下单时间元素"""
        return self.get_element(self.orderTimeElement)

    def get_star_data_times(self):
        """先清空日历中的开始日期，然后返回开始时间元素"""
        self.get_element(self.starDateTimesElement).clear()
        return self.get_element(self.starDateTimesElement)

    def get_end_data_times(self):
        """先清空日历中的结束日期，然后返回结束时间元素"""
        self.get_element(self.endDateTimesElement).clear()
        return self.get_element(self.endDateTimesElement)

    def get_choose_data_ok_button_box(self):
        """获取选择日期中的确认元素"""
        return self.get_element(self.chooseDataOkBottonElement)

    def get_input_order_num_box(self):
        """获取订单号输入框元素"""
        return self.get_element(self.inputOrderNumElement)

    def get_desk_id_box(self):
        """获取餐桌号/取餐号输入框元素"""
        return self.get_element(self.deskIdElement)

    def get_inquiry_button_box(self):
        """获取查询按钮元素"""
        return self.get_element(self.inquiryButtonElement)

    def get_reset_button_box(self):
        """获取重置按钮元素"""
        return self.get_elements(self.resetButtonElement)

    def get_order_detail_box(self):
        """订单-全部订单-搜索出来结果中的详情元素"""
        return self.get_element(self.orderDetailElement)

    def get_order_num_box(self):
        """订单-全部订单-搜索出来结果中的订单号元素"""
        return self.get_element(self.orderNumElement)

    def get_desk_id_num(self):
        """订单-全部订单-搜索出来结果中的餐桌号/订单号元素"""
        return self.get_element(self.deskIdNum)


OrderPage = OrderPage()
