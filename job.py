from selenium import webdriver

driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')

driver.implicitly_wait(10)

driver.get('https://www.51job.com')

driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_id('work_position_input').click()

citys = driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000 em[class=on]')


#此部分参照答案
for one in citys:

    one.click()
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

driver.find_element_by_id('work_position_click_bottom_save').click()


driver.find_element_by_css_selector('.ush  button').click()#为什么不用('.fltr button')


jobs = driver.find_elements_by_css_selector('#resultList  div.el')

for job in jobs:
    if 'title' in job.get_attribute('class'):
        continue

    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print (' | '.join(strField))

driver.quit()
