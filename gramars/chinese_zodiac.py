# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[1:5])
#
# print(chinese_zodiac[-1])

# year = int( input("请输入出生年份： ") )
# print(chinese_zodiac[year % 12])

# for year in range(2000, 2020):
    # print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))
import time
num = 5
while True:
    num += 1
    if num == 10:
        continue
    print(num)
    # time.sleep(1)

# print( '猪' in chinese_zodiac )
# print( '猪' not in chinese_zodiac )
#
# print( chinese_zodiac + chinese_zodiac );
# print( chinese_zodiac * 10 )
