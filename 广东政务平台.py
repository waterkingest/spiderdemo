from selenium import webdriver
from pyquery import PyQuery as pq
import csv
import time
#加载驱动
driver = webdriver.Chrome()
#获取网址
def getinformation(name):
    driver.get('http://pro.gdstc.gd.gov.cn/egrantweb/reg-organization/findOrgRegistered')
    #模仿用户输入关键字
    driver.find_element_by_xpath('//*[@id="orgName"]').send_keys(name)
    driver.find_element_by_xpath('//*[@value="查询"]').click()
    time.sleep(2)
    html=driver.page_source
    doc=pq(html)
    email=doc('#showOrgInfo > table:nth-child(6) > tbody > tr:nth-child(3) > td:nth-child(2)').text()
    phone=doc('#showOrgInfo > table:nth-child(6) > tbody > tr.li_2 > td:nth-child(2)').text()
    people=doc('#showOrgInfo > table:nth-child(6) > tbody > tr:nth-child(1) > td:nth-child(2)').text()
    str_temp={'name':str(name),'people':str(people),'email':email}
    print(str_temp)
    return str_temp
with open(r'D:\爬虫\第一单广佛\广佛.csv','r',encoding='utf-8')as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
            if reader.line_num==1:
                continue
            name=line[0].strip()
            massage=getinformation(str(name))
            with open(r'D:\爬虫\test.csv','a',newline='',encoding='utf-8')as csvf:
                fieldnames=['name','people','phone','email']
                write=csv.DictWriter(csvf,fieldnames=fieldnames)
                write.writerow(massage)
