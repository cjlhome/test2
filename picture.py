from selenium import webdriver

driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')

driver.implicitly_wait(5)

driver.get(' https://tinypng.com/ ')

driver.find_element_by_css_selector('section[class="target" ]').click()

import win32com.client
shell = win32com.client.Dispatch('wscript.shell')
shell.sendkeys('r C:\Users\Administrator\Pictures\微信图片_20181007184326.jpg'+'\n')
input('1')



iftrue = driver.find_element_by_css_selector('div[class="progress success"]')

for one in iftrue:
    if

pass