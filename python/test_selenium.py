from selenium import webdriver
import os
# 1.Basic visit web and input&click
    # the geckodriver is need for firefox
P1 = r'https://www.baidu.com'

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

searchBox = driver.find_element_by_id('kw')

searchBox.send_keys('what is python')

searchButton = driver.find_element_by_id('su')
searchButton.click()

