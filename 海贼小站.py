import requests
from threading import Thread
import re
import time
import json
import hashlib

class BaiDu:
    """
    爬取百度图片
    """
    def __init__(self):
        self.start_time = time.time()
        
        #self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&rn=60&'
        self.url = 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&a=read&zjid=115796'
        self.header = {'Host':'www.zerobyw4.com.','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
        self.header2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
        self.proxies = {'http':'27.184.245.4:8118','https':'27.184.245.4:8118'}
        self.num = 0

    def queryset(self):
        """
        将字符串转换为查询字符串形式
        """
        url = self.url
        self.getrequest(url)

    def getrequest(self, url):
        """
        发送请求
        """
        print('[INFO]: 开始发送请求：' + url)
        ret = requests.get(url, headers=self.header)
        time.sleep(2)
        if str(ret.status_code) == '200':
            print('[INFO]: request 200 ok :' + ret.url)
        else:
            print('[INFO]: request {}, {}'.format(ret.status_code, ret.url))

        response = ret.content.decode()
        #print(response)
        img_links = re.findall(r'<img class="" src="(.*)" alt', response)
        links = []
        #print (links)
        # 提取url
        for link in img_links:

            links.append(link[0:])

        self.thread(links)

    def saveimage(self, link):
        """
        保存图片
        """
        print('[INFO]:正在保存图片：' + link)
        # m = hashlib.md5()
        # m.update(link.encode())
        name = str(link)#m.hexdigest()
        name=name[-9:-4]
        ret = requests.get(link, headers = self.header2)
        image_content = ret.content
        filename = 'D:\\爬虫\\海贼小站\\image\\' + name + '.jpg'
        with open(filename, 'wb') as f:
            f.write(image_content)

        print('[INFO]:保存成功，图片名为：{}.jpg'.format(name))

    def thread(self, links):
        """多线程"""
        self.num +=1
        for i, link in enumerate(links):
            print('*'*50)
            print(link)
            print('*' * 50)
            if link:
                # time.sleep(0.5)
                t = Thread(target=self.saveimage, args=(link,))
                t.start()
                # t.join()
            self.num += 1
        print('一共进行了{}次请求'.format(self.num))

    def __del__(self):

        end_time = time.time()
        print('一共花费时间:{}(单位秒)'.format(end_time - self.start_time))

def main():
    #page = input('请输入你要爬取图片的页数(40张一页):')
    baidu = BaiDu()
    baidu.queryset()


if __name__ == '__main__':
    main()
