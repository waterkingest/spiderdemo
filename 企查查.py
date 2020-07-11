from selenium import webdriver
from pyquery import PyQuery as pq
import csv
import time
#加载驱动
driver = webdriver.Chrome()
driver.get('https://www.qichacha.com/')
time.sleep(20)
#获取网址
def getinformation(name):
    driver.get('https://www.qichacha.com/')
    #模仿用户输入关键字
    driver.find_element_by_xpath('//*[@id="searchkey"]').send_keys(name)
    driver.find_element_by_xpath('//*[@value="查一下"]').click()
    html=driver.page_source
    doc=pq(html)
    item=doc('#search-result > tr:nth-child(1) > td:nth-child(3) > a').attr('href')
    item=str(item)
    html2=('https://www.qichacha.com/'+item)
    driver.get(html2)
    detila=driver.page_source
    doc2=pq(detila)
    address=doc2('#company-top > div.row > div.content > div.dcontent > div:nth-child(2) > span.cvlu > a:nth-child(1)').text()
    email=doc2('#company-top > div.row > div.content > div.dcontent > div:nth-child(2) > span.fc > span.cvlu > a:nth-child(1)').text()
    phone=doc2('#company-top > div.row > div.content > div.dcontent > div:nth-child(1) > span.fc > span.cvlu > span').text()
    people=doc2('#ipoMember > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').text()
    str_temp={'name':str(name),'people':str(people),'phone':str(phone),'email':email,'address':address}
    print(str_temp)
    return str_temp
with open(r'D:\爬虫\广佛1422√.csv','r',encoding='UTF-8')as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
            if reader.line_num==1:
                continue
            name=line[0].strip()
            massage=getinformation(str(name))
            with open(r'D:\爬虫\广佛.csv','a',newline='',encoding='utf-8')as csvf:
                fieldnames=['name','people','phone','email','address']
                write=csv.DictWriter(csvf,fieldnames=fieldnames)
                write.writerow(massage)
