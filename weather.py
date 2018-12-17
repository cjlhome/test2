from selenium import webdriver


driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')



driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')



weainf = driver.find_element_by_id('forecastID')

print(weainf.text)

lowest = 60
lowestcity =[]

for one in weainf:
    print(one)
    city_wea = one.spilt('\n')[0]
    lowweather = one.split('/')[1]
    if lowweather < lowest:
        lowestcity = [lowweather]

    elif lowweather == lowest:
        lowestcity.append(city_wea)


print ('温度最低为%s℃，城市有%s' %(lowest,lowestcity))



