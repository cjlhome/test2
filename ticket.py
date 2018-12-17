from selenium import webdriver

driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')

driver.implicitly_wait(5)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')


ele = driver.find_element_by_id('fromStationText').click()

ele.send_keys('南京南\n')

to_ele = driver.find_element_by_id('toStationText').click()

to_ele.send_keys('杭州东\n')
#select下拉框选择
start_time = select(driver.find_element_by_id('cc_start_time'))

start_time.select_by_visible_text('06:00--12:00')

driver.find_element_by_css_selector('#date_range li:nth-child(2)').click()
#获取所以车次信息
trainno = driver.find_element_by_xpath('//*[@id="float"]/th[1]')
for one in trainno:
    print(one.text)
#获取所有二等座位且有票的信息

seats = driver.find_elements_by_css_selector('#queryLeftTable > tr')

#二等座的信息如何获取
for one in seats:


    print('one.text')

driver.quit()






