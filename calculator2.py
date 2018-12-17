from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'F:\androidapp\com.ibox.calculators_2.9.6_1296.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'#自己通过adb
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'#

desired_caps['unicodeKeyboard']  = True#自动化过程中需要输入中文的时候用
desired_caps['resetKeyboard']  = True#还原成以前的输入法
desired_caps['noReset'] = True#不用清掉APP之前所有的数据
desired_caps['newCommandTimeout'] = 6000#调试程序的时候APPIUM可能会断，所以可以设置这个时间长一点
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


try:
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.ibox.calculators:id/digit3').click()
    time.sleep(1)

    driver.find_element_by_id('com.ibox.calculators:id/plus').click()
    time.sleep(1)


    driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
    time.sleep(1)

    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    time.sleep(1)

    driver.find_element_by_id("com.ibox.calculators:id/mul").click()
    time.sleep(1)

    driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
    time.sleep(1)
    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    time.sleep(1)
    #注意必须把id写全才可以
    ret = driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]')

    print(ret.text)

    if ret.text == '60':
        print('结果正确')

    else:
        print('错误！')

except:
    print (traceback.format_exc())




input('**** Press to quit..')
driver.quit()



