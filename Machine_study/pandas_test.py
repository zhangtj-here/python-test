from pandas import Series,DataFrame
import pandas as pd
#
# # obj = pd.Series([4, 5, 6, -1])
# # print(obj)
# obj = Series([4, 5, 6, -1])
# print(obj)
# print(obj.index)
# print(obj.values)

# {['a']: 1}
# {'a': [1]}

# obj2 = Series([4, 6, -0, 3], index=['d', 'b', 'c', 'a'])
# print(obj2)
# obj2['c'] = 6
# print(obj2)
# print('a' in obj2)
#
# print('f' in obj2)


sdata = {'beijing': 35000, 'shanghai': 71000}
obj3 = Series(sdata)
print(obj3)

obj3.index = ['bj', 'sh']
print(obj3)
