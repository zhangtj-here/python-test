
import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# print(b'\xc2\xbb'.decode('utf-8'))
# print('\u00bb')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from urllib import request
from urllib import parse

url = 'http://www.baidu.com'



response = request.urlopen(url,timeout=1)
print(response.read().decode('utf-8')) # 设置utf-8编码
