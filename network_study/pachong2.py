from urllib import parse
from urllib import request


data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
# print(data)

# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get', timeout=2)
print(response2.read().decode('utf-8'))

import urllib
import socket

try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
# print(response3.read().decode('utf-8'))