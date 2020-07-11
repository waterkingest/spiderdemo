import urllib.request
import xlwt
import re
import urllib.parse
from lxml import etree
import requests
import csv

#模拟浏览器
header={
    'Host':'search.51job.com',
    'Referer':'https://mkt.51job.com/tg/sem/pz_2018.html?from=baidupz',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 37abc/2.0.6.16 Chrome/60.0.3112.113 Safari/537.36'
}

def getfront(page,item):

     result = urllib.parse.quote(item)
     ur1 = result+',2,'+ str(page)+'.html'
     ur2 = 'http://search.51job.com/list/000000,000000,0000,00,9,99,'
     res = ur2+ur1
     a = urllib.request.urlopen(res)
     html = a.read().decode('gbk')          # 读取源代码并转为unicode
     return html

def getInformation(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)" href="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>.*?',re.S)#匹配换行符
    items=re.findall(reg,html)
    return items


excel1 = xlwt.Workbook()
# 设置单元格
sheet1 = excel1.add_sheet('Job', cell_overwrite_ok=True)
sheet1.write(0, 0, '序号')
sheet1.write(0, 1, '职位')
sheet1.write(0, 2, '公司名称')
sheet1.write(0, 3, '公司地点')
sheet1.write(0, 4, '公司性质')
sheet1.write(0, 5, '薪资')
sheet1.write(0, 6, '学历要求')
sheet1.write(0, 7, '工作经验')
sheet1.write(0, 8, '公司规模')
sheet1.write(0, 9, '公司类型')
sheet1.write(0, 10,'公司福利')
sheet1.write(0, 11,'发布时间')
sheet1.write(0, 12,'任职要求')
sheet1.write(0,13,'人数')
sheet1.write(0,14,'职能类型')


number = 1
item='新闻'
for j in range(1,51):
    try:
            print("正在爬取第"+str(j)+"页数据...")
            html = getfront(j,item)      #调用获取网页原码
            for i in getInformation(html):
                try:
                    url1 = i[1]
                    url2 = i[3]
                    res1 = requests.get(url=url1,headers=header)
                    res2 = requests.get(url=url2,headers=header)
                    res1.encoding = res1.apparent_encoding
                    res2.encoding = res2.apparent_encoding
                    res1=res1.text
                    res2=res2.text
                    s1 = etree.HTML(res1)  # 将源码转化为能被 XPath 匹配的格式
                    s2 = etree.HTML(res2)
                    persons = s2.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/text()')[1].strip()
                    comyany_avlue = s2.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/text()')[0].strip()
                    experience = s1.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[1].strip()
                    education = s1.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[2].strip()
                    comyany_type = s2.xpath('/html/body/div[2]/div[2]/div[2]/div/p/a/text()')
                    welface = re.findall(re.compile(r'<span class="sp4">(.*?)</span>',re.S),res1)
                    requir = s1.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/p/text()')
                    renshu=s1.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[3].strip()
                    zhineng=s1.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p[1]/a/text()')
                    #comyany_avlue=comyany_avlue.encode().decode('unicode_escape')
                    #experience =experience.encode().decode('unicode_escape')
                    #education=education.encode().decode('unicode_escape')
                    #comyany_type=comyany_type.encode().decode('unicode_escape')
                    #experience=experience.encode().decode('unicode_escape')
                    print(i[0],i[2],i[4],i[5],comyany_avlue,experience,education,persons,comyany_type,zhineng,welface,renshu,i[6])
                    sheet1.write(number,0,number)
                    sheet1.write(number,1,i[0])
                    sheet1.write(number,2,i[2])
                    sheet1.write(number,3,i[4])
                    sheet1.write(number,4,comyany_avlue)
                    sheet1.write(number,5,i[5])
                    sheet1.write(number,6,education)
                    sheet1.write(number,7,experience)
                    sheet1.write(number,8,persons)
                    sheet1.write(number,9,comyany_type)
                    sheet1.write(number,10,("  ".join(str(i) for i in welface)))
                    sheet1.write(number,11,i[6])
                    sheet1.write(number,12,requir)
                    sheet1.write(number,13,renshu)
                    sheet1.write(number,14,zhineng)
                    number+=1
                except:
                    pass
    except:
        pass

excel1.save("新闻.xls")
