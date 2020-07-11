from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo
from config import *
import time
import csv
browser = webdriver.Chrome()
url1 = ('https://steamcommunity.com/market/search?appid=730#p')
def get_managers():
    for j in range(1,1479):
        url=url1+str(j)+'_name_asc'
        browser.get(url)
        if j==1:
            b=input()
        time.sleep(5)            
        html = browser.page_source
        doc = pq(html)
        for i in range (0,9):
            i=str(i)
            product = {
            'name':doc('#result_'+ i +'_name').text(),
            'price':doc('#result_'+ i + '> div.market_listing_price_listings_block > div.market_listing_right_cell.market_listing_their_price > span.market_table_value.normal_price > span.normal_price').text(),           
                }
            print(product)
            with open('steam.csv', 'a',encoding='utf-8',newline='') as csvfile:
                fieldnames = [ 'name', 'price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(product)
        #browser.find_element_by_xpath('//*[@class="pagebtn"]').click()
if __name__ == '__main__':
        get_managers()
        broswer.close()

