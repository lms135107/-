# - 点击搜索按钮
# - 输入“无线”
# - 获取当前有几条记录?
from appium import webdriver

import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
#解决中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.android.settings:id/search').click()
driver.find_element_by_id('android:id/search_src_text').send_keys('无线')
ele_result=driver.find_elements_by_xpath("//*[contains(@resource-id,'com.android.settings:id/title')]")
print(len(ele_result))
