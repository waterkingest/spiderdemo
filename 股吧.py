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
url='http://guba.eastmoney.com/list,zssh000001_'
erro=[]
for i in range(10169,10199):
    print('开始爬第'+str(i)+'页')
    try:
        url1=url+str(i)+'.html'
        driver.get(url1)
        time.sleep(1)
        html=driver.page_source
        doc=pq(html)
        for j in range(2,81):
            j=str(j)
            read=doc('#articlelistnew > div:nth-child('+j+') > span.l1.a1').text()
            pinglun=doc('#articlelistnew > div:nth-child('+j+') > span.l2.a2').text()
            title=doc('#articlelistnew > div:nth-child('+j+') > span.l3.a3 > a').text()
            auther=doc('#articlelistnew > div:nth-child('+j+') > span.l4.a4 > a > font').text()
            time1=doc('#articlelistnew > div:nth-child('+j+') > span.l5.a5').text()
            massage={
                'read':read,
                'pinglun':pinglun,
                'title':title,
                'auther':auther,
                'time':time1
            }
            print(massage)
            with open(r'D:\爬虫\股吧\下半年.csv','a',newline='',encoding='utf-8')as csvf:
                fieldnames=['read','pinglun','title','auther','time']
                write=csv.DictWriter(csvf,fieldnames=fieldnames)
                write.writerow(massage)
    except:
        print('第'+str(i)+'页出错')
        erro.append(i)
        print(erro)
        pass
for k in erro:
    print('开始爬第'+str(k)+'页')
    try:
        url2=url+str(k)+'.html'
        driver.get(url2)
        time.sleep(1)
        html2=driver.page_source
        doc2=pq(html2)
        for g in range(2,81):
            g=str(g)
            read=doc2('#articlelistnew > div:nth-child('+g+') > span.l1.a1').text()
            pinglun=doc2('#articlelistnew > div:nth-child('+g+') > span.l2.a2').text()
            title=doc2('#articlelistnew > div:nth-child('+g+') > span.l3.a3 > a').text()
            auther=doc2('#articlelistnew > div:nth-child('+g+') > span.l4.a4 > a > font').text()
            time1=doc2('#articlelistnew > div:nth-child('+g+') > span.l5.a5').text()
            massage={
                'read':read,
                'pinglun':pinglun,
                'title':title,
                'auther':auther,
                'time':time1
            }
            print(massage)
            with open(r'D:\爬虫\股吧\下半年2.csv','a',newline='',encoding='utf-8')as csvf:
                fieldnames=['read','pinglun','title','auther','time']
                write=csv.DictWriter(csvf,fieldnames=fieldnames)
                write.writerow(massage)
    except:
        print('第'+str(k)+'页出错')
        erro.append(k)
        print(erro)
        pass