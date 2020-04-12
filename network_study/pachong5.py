# get请求
import requests
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.get(url, data)
print(response.text)

# post请求
url = "http://httpbin.org/post"
data = {'key': 'value', 'abc': 'xyz'}
response1 = requests.post(url,data)
print(response1.json())