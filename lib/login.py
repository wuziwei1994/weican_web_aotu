# author:吴紫葳
# times:2020/7/9 9:24
# # coding:-*- utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome(r'D:\weican_web_aotu\chromedriver.exe')

merchant_id = '539848'
account = 'wct'
password = '123456'
driver.get('http://b.local.weicantimes.com/login')


def login():
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/form/div[1]/div/input').send_keys(merchant_id)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/form/div[2]/div/input').send_keys(account)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/form/div[3]/div/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/form/div[4]/div/input').send_keys('1')
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/form/div[6]/div[1]/input').click()

