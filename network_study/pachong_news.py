from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'https://news.cnblogs.com/'
# 取得新闻的标题
def craw2(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for title_href in soup.find_all('h2', class_='news_entry'):
        print([title.string
               for  title in title_href.find_all('a') if title.string])

craw2(url)

import threading
import time
from threading import current_thread
# _thread

def myThread(arg1, arg2):
    url = 'https://news.cnblogs.com/n/page/' + str(arg1)
    craw2(url)
    print(url)
    print(arg1)


# for i in range(1, 6, 1):
#     # t1 = myThread(i, i+1)
#     # print(i)



print(current_thread().getName(), 'end')

# 翻页
for i in range(2, 11, 1):
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()