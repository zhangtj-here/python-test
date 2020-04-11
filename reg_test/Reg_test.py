import re
# . ^ $ * + ? {m} {m,n} [] | \d \D \s ()
# ^s
#  .*?

# p = re.compile('ca*t') # 匹配前面的字符出现0次到多次
# print(p.match('caaaat'))
# print(p.match('ct'))


# p = re.compile('ca+t') # 匹配前面的字符出现1次到多次
# print(p.match('caaaat'))
# print(p.match('cat'))

# p = re.compile('ca?t') # 匹配前面的字符出现0次到1次
# print(p.match('ct'))
# print(p.match('cat'))

# p = re.compile('ca{1,5}t') # 匹配{m}出现m的次数,{m,n}匹配出现m到n中的任意值次数包括m,n
# print(p.match('caaaat'))
# print(p.match('cat'))

# p = re.compile('ca[bvm][abc]t') # []中括号中的任意一个字符匹配成功，都可以匹配成功
# print(p.match('caapt'))
# print(p.match('cabbt'))

# p = re.compile('ca(aa|bb)t') # |匹配左边或者右边，通常和括号配合
# print(p.match('caaat'))
# print(p.match('cabbt'))


# p = re.compile('ca\Dt') # \d 表示一位数字，等同[0-9],[1234567890] \D 表示以为非数字
# print(p.match('caat'))
# print(p.match('ca2t'))

# p = re.compile(r'ca\st') # \s 表示一个空格，\S表示非空格
# print(p.match('caat'))
# print(p.match('ca1t'))


# p = re.compile('ca\Dt') # () 表示分组
# print(p.match('caat'))
# print(p.match('ca2t'))






# p = re.compile('^$') # ^$ 表示空行
# print(p.match(''))
# print(p.match(' '))

# p = re.compile(r'(\d{1,4})-(\d+)-(\d+)') # () 表示分组
# print(p.match('2018-05-10').groups())
# print(p.match('2018-05-10').group(1))
# print(p.match('2018-05-10').group(2))
# print(p.match('2018-05-10').group(3))
# year, month, day = p.match('2018-05-10').groups()
# print(year, month, day)
# print(p.match('18-05-10'))

# p = re.compile(r'(\d{1,4})-(\d+)-(\d+)') # () 表示分组
# print(p.search('aa20a18-05-1a0bb').groups()) # serach 表示搜索匹配
# print(p.match('2018-05-10').group(1))


phone = '123-456-789 # 这是电话号码'
# p = re.sub('#.*$', '', phone) # sub用于正则匹配替换，类似于js里的replace
# print(p)


# p = re.sub(r'\S', '1', phone) # sub用于正则匹配替换，类似于js里的replace
# print(p)

# p1 = re.search('(\d+)-(\d+)-(\d+)', 'aa123-456-789bb')
# print(p1.groups())

p1 = re.findall('\d+', 'aa123-456-789bb')  # findall全局匹配，类似于js正则里面//g
print(p1)
# findall()
# p1 = re.compile('.{3}') #.表示任意字符
# print(p1.match('a*^'))
#
# p2 = re.compile('jpg$') #^以什么开头 $以什么结尾
# print(p2.match('123.jpg'))

