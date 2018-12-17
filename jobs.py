from selenium import webdriver

driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')

driver.implicitly_wait(6)

driver.get('https://www.51job.com')

driver.find_element_by_css_selector('div.ush>a').click()

driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_id('work_position_input').click()
#取消已经选择的城市,这里为什么要写一个for循环，可以直接点击现在已经选中的那个元素id取消掉选择，然后在去点击杭州这个元素的id不就可以了吗？
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')

for one in selectedCityEles:
    one.click()

#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

driver.find_element_by_id('work_position_click_bottom_save').click()

driver.find_element_by_id('funtype_click').click()


driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()

driver.find_element_by_id('funtype_click_bottom_save').click()
#公司性质
driver.find_element_by_id('cottype_list').click()
#这句还有其他写法么？
#driver.find_element_by_css_selector('span[data-value="01"]')这种写法可以么？
driver.find_element_by_css_selector('#cottype_list.span li[data-value="01"]').click()
driver.find_element_by_id('workyear_list').click()

driver.find_element_by_css_selector('#workyear_list.span li[data-value="02"]').click()

driver.find_element_by_css_selector('div.p_sou > span.p_but').click()#思考其他写法


jobs = driver.find_elements_by_id('#resultList > div[class=e1]')

for job in jobs:
    fields = job.find_elements_by_tag_name('span')

    stringFilelds = [field.text for field in fields]#这二句代码没有看懂，可以直接写成
                                                    #fields = jobs.find_elements_by_tag_name('span').text吗？
    print (' | '.join(stringFilelds))


driver.quit()


