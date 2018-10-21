# 爬虫实战
import requests
from bs4 import BeautifulSoup

class downLoader(object):
    def __init__(self):


if __name__ == '__main__':
    # 爬取一章的内容
    # target = 'http://www.biqukan.com/1_1094/5403177.html'
    # req = requests.get(url=target)
    # html = req.text
    # bf = BeautifulSoup(html)#创建一个Beautiful Soup对象参数为html文本
    # texts = bf.find_all('div', class_ = 'showtxt')
    # content = texts[0].text.replace('\xa0'*8,'\n\n')
    #爬取每张标题及其内容
    urls = 'http://www.biqukan.com/1_1094/'
    __get = requests.get(url=urls)
    bf = BeautifulSoup(__get.text)
    div = bf.findAll('div', class_ = 'listmain')
    a = BeautifulSoup(str(div))
    __a = a.find_all('a')
    for item in __a:
        print(item.string, item.get('href'))
