from bs4 import BeautifulSoup
import requests
import os
import shutil
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'http://www.cnu.cc/discoveryPage/hot-人像'


# 下载图片
# Requests 库封装复杂的接口，提供更人性化的 HTTP 客户端，但不直接提供下载文件的函数。
# 需要通过为请求设置特殊参数 stream 来实现。当 stream 设为 True 时，
# 上述请求只下载HTTP响应头，并保持连接处于打开状态，
# 直到访问 Response.content 属性时才开始下载响应主体内容


def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


# 取得演讲图片
# def craw3(url):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'lxml')
#     for pic_href in soup.find_all('div', class_='grid-item work-thumbnail'):
#         for pic in pic_href.find_all('img'):
#             imgurl = re.sub(r'\?.*', '',pic.get('src'))
#             dir = os.path.abspath('./imgAdd')
#             filename = os.path.basename(imgurl)
#             imgpath = os.path.join(dir, filename)
#             print('开始下载 %s' % imgurl)
#             download_jpg(imgurl, imgpath)

def craw3(url):
    content = requests.get(url, headers=headers).text
    pattern = re.compile(r'<a href=.*?title">(.*?)</div>.*?author">(.*?)</div>.*?src="(.*?)".*?</a>', re.S)
    results = re.findall(pattern, content)
    for result in results:
        (title, author, pic) = result
        imgurl = re.sub(r'\?.*', '', pic)
        # titleName = re.sub('\s|\"', '', title) + '.jpg'
        titleName = re.sub('\s|\"|\||\/', '', title) + '(拍摄人-'+ re.sub('\s|\"|\||\/', '', author)  + ')' '.jpg'
        dir = os.path.abspath('./imgAdd')
        filename = os.path.basename(imgurl)
        imgpath = os.path.join(dir, titleName)
        # imgpath = os.path.join(dir, filename)
        print('开始下载 %s' % imgurl)
        download_jpg(imgurl, imgpath)


# craw3(url)
#

import threading
import time
from threading import current_thread
def myThread(arg1, arg2):
    url = 'http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F?page=' + str(arg1)
    craw3(url)
    print('第 %d 页' % arg1)
# 翻页

for i in range(1, 8, 1):
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()
