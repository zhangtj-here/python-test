# 读取人物名字
# f = open('name.txt')
# data = f.read()
# print(data.split('|'))
#
# # 读取兵器名称
# f2 = open('weapon.txt')
# # data2 = f2.read()
# # print(data2)
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1
#
#
# f3 = open('sanguo.txt', encoding="GBK")
# print(f3.read().replace('\n', ''))

def func(filename):
    print(open(filename).read())

func('name.txt')
func('weapon.txt')
func('sanguo.txt')