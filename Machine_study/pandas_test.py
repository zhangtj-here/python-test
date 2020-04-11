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


# sdata = {'beijing': 35000, 'shanghai': 71000}
# obj3 = Series(sdata)
# print(obj3)
#
# obj3.index = ['bj', 'sh']
# print(obj3)

data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2016, 2017],
        'pop':  [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
# print(frame)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)
# print(frame2['city'])
# print(frame2.city)
# print(frame2.year)

frame2['new'] = 100
# frame2.new = 200

# print(frame2)

# frame2['cap'] = frame2.city == 'beijing'

# print(frame2)

pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008:2.0, 2009: 3.6}
      }


frame3 = DataFrame(pop)
# print(frame3.T)


# obj5 = Series([5.5, 7.7, -0.1, 3.7], index=['b', 'd', 'c', 'a'])
# obj6 = obj5.reindex(['a', 'b', 'c', 'd', 'e','f','g'],fill_value=0)
# print(obj6)
obj7 = Series(['blue', 'purple', 'yellow'], index=[0,2,4])
# print(obj7.reindex(range(6), method='ffill'))

from numpy import nan as NA
data = Series([1, NA, 2])
# print(data.dropna())

data2 = DataFrame([[1, 6.5, 3], [1., NA, NA], [NA, NA, NA]])
data2[4] = NA
print(data2)
# print(data2.dropna(how='all'))
print(data2.dropna(axis=1, how='all'))
print(data2.fillna(0,inplace=True))
print(data2)