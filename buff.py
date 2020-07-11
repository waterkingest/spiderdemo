from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo
from config import *
import time
import csv
browser = webdriver.Chrome()
url1 = ('https://buff.163.com/market/?game=csgo#tab=selling&page_num=1')
def get_managers():
    browser.get(url1)
    time.sleep(30)
    while True:        
        time.sleep(3)            
        html = browser.page_source
        doc = pq(html)
        for i in range (1,20):
            i=str(i)
            product = {
            'name':doc('#j_list_card > ul > li:nth-child'+'('+ i + ')' +' > h3 > a').text(),
            'price':doc('#j_list_card > ul > li:nth-child'+'('+ i + ')' +' > p > strong').text(),           
                }
            print(product)
            with open('buff.csv', 'a',encoding='utf-8',newline='') as csvfile:
                fieldnames = [ 'name', 'price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(product)
        browser.find_element_by_xpath('//*[@class="page-link next"]').click()
if __name__ == '__main__':
        get_managers()
        broswer.close()
