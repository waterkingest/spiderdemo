from selenium import webdriver
from pyquery import PyQuery as pq
import csv
import time
#加载驱动
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 设置headless模型
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
#获取网址
erro=[]
def getinformation(name):
    driver.get('http://search.mtime.com/search/?q=%E5%90%B4%E4%BA%AC&t=0')
    #模仿用户输入关键字
    driver.find_element_by_xpath('//*[@id="searchRegion"]/input[1]').clear()
    driver.find_element_by_xpath('//*[@id="searchRegion"]/input[1]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="searchRegion"]/input[2]').click()
    time.sleep(3)
    html=driver.page_source
    doc=pq(html)
    item=doc('#moreRegion > li > h3 > a').attr('href')
    url_detail = str(item)
    driver.get(url_detail)
    time.sleep(3)
    html_detail = driver.page_source
    doc2 = pq(html_detail)
    title=doc2('#db_head > div.db_ihead > div > div.clearfix > h1').text()
    director=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > dl > dd:nth-child(1) > a').text()
    try:
        actor1=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(2) > dd > p:nth-child(2) > a').text()
        actor2=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(3) > dd > p:nth-child(2) > a').text()
        actor3=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(4) > dd > p:nth-child(2) > a').text()
        movietype1=doc2('#db_head > div.db_ihead > div > div.otherbox.__r_c_ > a:nth-child(2)').text()
        movietype2=doc2('#db_head > div.db_ihead > div > div.otherbox.__r_c_ > a:nth-child(3)').text()
        people0=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > dl > dd:nth-child(1) > a').attr('href')
        people1=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(2) > dd > p:nth-child(2) > a').attr('href')
        people2=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(3) > dd > p:nth-child(2) > a').attr('href')
        people3=doc2('#movie_warp > div.db_bodyout > div.db_shadow > div > div.db_contout > div.db_cont > div.clearfix.zoom > div.base_r > div.clearfix.pt15 > div > dl:nth-child(4) > dd > p:nth-child(2) > a').attr('href')
        actor=[str(people0),str(people1),str(people2),str(people3)]
        movies=['','','','']
        nominat=['','','','']
        praise=['','','','']
        for i in range(0,4):
            it1=actor[i]+'filmographies/'
            driver.get(it1)
            time.sleep(3)
            p1=driver.page_source
            p1d=pq(p1)
            movies[i]=p1d('#leftCounter').text()
            driver.get(actor[i]+'awards.html')
            time.sleep(3)
            p2=driver.page_source
            p2d=pq(p2)
            praise[i]=p2d('body > div.per_outer > div > h3 > strong:nth-child(1)').text()
            nominat[i]=p2d('body > div.per_outer > div > h3 > strong:nth-child(2)').text()
            print(praise,nominat)
    except:
        erro.append(name)
        pass
    str_temp={'name':title,'director':director,'directorprice':praise[0],'directornominat':nominat[0],'directormovies':movies[0],'movietype':movietype1+'/'+movietype2,'actor1':actor1,'praise1':praise[1],'nominat1':nominat[1],'movies1':movies[1],'actor2':actor2,'praise2':praise[2],'nominat2':nominat[2],'movies2':movies[2],'actor3':actor3,'praise3':praise[3],'nominat3':nominat[3],'movies3':movies[3]}
    print(str_temp)
    return str_temp
with open(r'D:\爬虫\电影\电影.csv','r',encoding='utf-8')as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
            if reader.line_num==1:
                continue
            name=line[0].strip()
            massage=getinformation(str(name))
            with open(r'D:\爬虫\电影\数据3.csv','a',newline='',encoding='utf-8')as csvf:
                fieldnames=['name', 'director','directorprice','directornominat','directormovies', 'movietype', 'actor1', 'praise1', 'nominat1', 'movies1', 'actor2', 'praise2', 'nominat2', 'movies2', 'actor3', 'praise3', 'nominat3','movies3']
                write=csv.DictWriter(csvf,fieldnames=fieldnames)
                write.writerow(massage)
print(erro)
