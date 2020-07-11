from selenium import webdriver
from pyquery import PyQuery as pq
import csv
import time
from lxml import etree
from selenium.webdriver.common.keys import Keys
#加载驱动
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 设置headless模型
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
#获取网址
def writefile(aa):
    with open(r'D:\爬虫\酒店评论\评论4.csv','a',newline='',encoding='utf-8')as csvf:
        fieldnames=['hotel','address','name','ct-title','contentype','score','conten','time']
        write=csv.DictWriter(csvf,fieldnames=fieldnames)
        write.writerow(aa)
def getinformation(url):
    print(url)
    driver.get(url)
    #模仿用户输入关键字
    time.sleep(2)
    for i in range(6):
        time.sleep(2)
        html=driver.execute_script("return document.documentElement.outerHTML")
        li=etree.HTML(html)
        for j in range(1,11):
            j=str(j)  
            hotel=li.xpath('//div[@class="name_cont"]/p[1]/text()')
            address=li.xpath('//div[@class="name_cont"]/p[2]/text()')
            name=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[1]/p/a/text()')
            try:
                ct_title=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[2]/p/text()')
            except:
                ct_title=[' ','']
            try:
                contentype=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[2]/div[2]/div/span[2]/text()')
            except:
                contentype=[' ','']
            try:
                content=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[2]/div[3]/p/text()')
            except:
                content-[' ','']
            try:
                score=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[2]/div/div/p[3]/text()')
            except:
                score=[' ','']
            try:
                time1=li.xpath('//div[@class="cmt-list"]/div['+j+']/div[2]/p[2]/span[1]/text()')
            except:
                time1=[' ',''] 
            print(contentype)
            ww={'hotel':hotel,
            'address':address,
            'name':name,
            'ct-title':ct_title,
            'contentype':contentype,
            'score':score,
            'conten':content,
            'time':time1
            }
            print(ww)
            writefile(ww)
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/section[2]/aside[1]/aside[3]/div/div/div/div[4]/div/div/div/div[3]').click()
        except:
            print(hotel[0])
with open(r'D:\爬虫\酒店评论\连接.csv','r',encoding='utf-8')as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
            if reader.line_num==1:
                continue
            url=line[0].strip()
            getinformation(str(url))
driver.close()

