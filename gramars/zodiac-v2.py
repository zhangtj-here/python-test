zodiac_name = ( u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
                u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座' )
zodiac_days = ( (1, 20), (2, 19), (3, 20), (4, 20), (5, 21), (6, 21),
                (7, 22), (8, 23), (9, 23), (10, 23), (11, 22), (12, 21) )
int_month = int(input("请输入月份："))
int_day = int(input("请输入日期："))
if int_month > 12 or int_day > 31:
    print('输入日期不合法')
    # return none
# print(type(int_month))
# (month, day) = (3, 15)
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 21:
#         print(zodiac_name[0])
#         break
n = 0
while zodiac_days[n] < (int_month, int_day):
    if int_month == 12 and int_day > 21:
        break
    n += 1
print(zodiac_name[n])

# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# zodiac_len = len(list(zodiac_day))
# print(zodiac_name[zodiac_len % 12])

