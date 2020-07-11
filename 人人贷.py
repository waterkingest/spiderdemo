from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo
from config import *
import time
import csv
browser = webdriver.Chrome()
url1 = ('https://www.renrendai.com/loan-')
def get_managers():
    for j in range(796990,797500):
        url = url1 + str(j) + '.html'
        browser.get(url)
        if j==796990 :
            time.sleep(30)
        html = browser.page_source
        doc = pq(html)
        nicheng= doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(1) > a').text()
        price=doc('#loan-transfer-detail > div > div.loan-content > div.loan-con-l.loan-alone-style > div.loan-l-number > p.w285 > em').text()
        name=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(3) > em').text()
        ID=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(4) > em').text()
        sex=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(5) > em').text()
        phone=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(6) > em').text()
        age=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(7) > em').text()
        qualification=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(8) > em').text()
        marriage=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(9) > em').text()
        salary=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(10) > em').text()
        house=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(11) > em').text()
        fangdai=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(12) > em').text()
        car=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(13) > em').text()
        chedai=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(14) > em').text()
        company=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(15) > em').text()
        companysize=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(16) > em').text()
        vocation=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(17) > em').text()
        city=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(18) > em').text()
        other=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li.w-680 > em').text()
        times=doc('#lend-loan > div > div > div.wdt-lend-info > div > div.loan-user-info > ul:nth-child(1) > li:nth-child(19) > em').text()
        product = {
            'name': name,
            'price':price,
            'nicheng':nicheng,
            'ID':ID,
            'sex':sex,
            'phone':phone,
            'age':age,
            'qualification':qualification,
            'marriage':marriage,
            'salary':salary,
            'house':house,
            'fangdai':fangdai,
            'car':car,
            'chedai':chedai,
            'company':company,
            'companysize':companysize,
            'vocation':vocation,
            'city':city,
            'time':times,
            'other':other,
                }
        print(product)
        with open('renrendai.csv', 'a',encoding='utf-8',newline='') as csvfile:
            fieldnames = [ 'name', 'price','nicheng','ID','sex','phone','age','qualification','marriage','salary','house','fangdai','car','chedai','company','companysize','vocation','city','time','other']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(product)
if __name__ == '__main__':
        get_managers()
        broswer.close()
