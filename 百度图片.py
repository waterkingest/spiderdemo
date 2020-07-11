import requests
from threading import Thread
import re
import time
import hashlib

class BaiDu:
    """
    爬取百度图片
    """
    def __init__(self, name, page):
        self.start_time = time.time()
        self.name = name
        self.page = page
        #self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&rn=60&'
        self.url = 'https://image.baidu.com/search/acjson'
        self.header = {}# 添加为自己的
        self.num = 0

    def queryset(self):
        """
        将字符串转换为查询字符串形式
        """
        pn = 0
        for i in range(int(self.page)):
            pn += 60 * i
            name = {'word': self.name, 'pn': pn, 'tn':'resultjson_com', 'ipn':'rj', 'rn':60}
            url = self.url
            self.getrequest(url, name)

    def getrequest(self, url, data):
        """
        发送请求
        """
        print('[INFO]: 开始发送请求：' + url)
        ret = requests.get(url, headers=self.header, params=data)

        if str(ret.status_code) == '200':
            print('[INFO]: request 200 ok :' + ret.url)
        else:
            print('[INFO]: request {}, {}'.format(ret.status_code, ret.url))

        response = ret.content.decode()
        img_links = re.findall(r'thumbURL.*?\.jpg', response)
        links = []
        # 提取url
        for link in img_links:

            links.append(link[11:])

        self.thread(links)

    def saveimage(self, link):
        """
        保存图片
        """
        print('[INFO]:正在保存图片：' + link)
        m = hashlib.md5()
        m.update(link.encode())
        name = m.hexdigest()
        ret = requests.get(link, headers = self.header)
        image_content = ret.content
        filename = 'D:\爬虫\百度图片\image' +'\ ' + name + '.jpg'
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
    name = input('请输入你要爬取的图片类型: ')
    page = input('请输入你要爬取图片的页数(60张一页):')
    baidu = BaiDu(name, page)
    baidu.queryset()


if __name__ == '__main__':


    main()
