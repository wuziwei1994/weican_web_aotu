# author:吴紫葳
# times:2020/7/16 14:17
# # coding:-*- utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome(r'D:\weican_web_aotu\chromedriver.exe')
driver.get('http://b.local.weicantimes.com/login')
chooseLanguage =driver.find_elements_by_css_selector('ul >li')
for o in chooseLanguage:
    o


