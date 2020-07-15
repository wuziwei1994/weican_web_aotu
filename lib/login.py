# author:吴紫葳
# times:2020/7/9 9:24
# # coding:-*- utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome(r'D:\weican_web_aotu\chromedriver.exe')

# 门店相关信息
merchant_id = '539848'
account = 'wct'
password = '123456'
driver.get('http://b.local.weicantimes.com/login')
driver.maximize_window()

time.sleep(2)
# 输入门店相关登录信息
input = driver.find_elements_by_css_selector('input.login-input-full')
for i in input:
    if '请输入商家编号' in i.get_attribute('placeholder'):
        i.send_keys(merchant_id)
    elif '请输入账号' in i.get_attribute('placeholder'):
        i.send_keys(account)
    elif '请输入密码' in i.get_attribute('placeholder'):
        i.send_keys(password)
        break
# 点击登录
driver.find_element_by_css_selector('input.login-form-login').click()

#循环点击title的每一个选项
time.sleep(3)
title = driver.find_elements_by_css_selector('div.navbar-contents a')
for i in title:
    time.sleep(1)
    i.click()


time.sleep(5)
driver.quit()
