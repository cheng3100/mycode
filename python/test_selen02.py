from selenium import webdriver
 
# 2.Basic visit and login
P1 = r'https://www.baidu.com'

driver = webdriver.Firefox()
driver.get(P1)

loginB = driver.find_element_by_name('tj_login')
loginB.click()

loginB2 = driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
loginB2.click()

userName = driver.find_element_by_id('TANGRAM__PSP_10__userName')
userName.send_keys('cheng6709')

passWd = driver.find_element_by_id('TANGRAM__PSP_10__password')
passWd.send_keys('hfut3015776')
