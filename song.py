from selenium import webdriver


driver = webdriver.Chrome(r'F:\tools\webdriver\chromedriver.exe')



driver.get('http://music.baidu.com/top/new')


div = driver.find_element_by_id('songListWrapper')


songList = div.find_elements_by_tag_name('li')


for li in songList:
     upTags = li.find_elements_by_class_name('up')
     up =[]
     if 'up' in upTags:
         title = li.find_element_by_class_name('song-title')
         songtitle = title.find_element_by_tag_name('a').text
         singers = li.find_element_by_class_name('author_list').text
        
         print('{:10s}:{}'.format(songtitle,singers))
  
driver.quit()











