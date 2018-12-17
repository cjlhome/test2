from selenium import webdriver

driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')

driver.implicitly_wait(5)

driver.get('https://www.vmall.com/')

driver.find_element_by_css_selector('a[href="http://www.honor.cn/"]').click()

eles = driver.find_elements_by_css_selector(".nav-cnt > *li")
#参考答案，检查是否包含了以下这些界面元素
expected = '智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'
for ele in eles:
    if eles = = expected:


    print('正确')


#返回主页检查
close()

expected = '''平板电脑|笔记本电脑|笔记本配件'''
from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)

ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

 eles = driver.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')


driver.quit()

