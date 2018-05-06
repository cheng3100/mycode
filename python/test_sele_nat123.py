from selenium import webdriver
 
# 2.Basic visit and login
P1 = r'http://www.nat123.com'

driver = webdriver.Firefox()
driver.get(P1)


userName = driver.find_element_by_id('txtname')
userName.send_keys('cheng3100')

passWd = driver.find_element_by_id('txtpwd')
passWd.send_keys('flycat3100')

loginB = driver.find_element_by_id('btnLogin')
loginB.click()
