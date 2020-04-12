import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>.*?author">(.*?)</div>', re.S)
results = re.findall(pattern, content)

print(results)

for result in results:
    url, name, author= result
    print(url, re.sub('\s', '', name), re.sub('\s', '', author))