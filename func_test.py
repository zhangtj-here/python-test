# print(123)
# print(123)
#
# def func (a, b, c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
# # func(1, c=2)
#
# def howlong(first, *other):
#     return 1 + len(other)
#
# print(howlong())

# var1 = 123
#
# def func ():
#     global var1
#     var1 = 456
#     print(var1)
# func()
# print(var1)

# list1 = [1, 2, 3]
# it = iter(list1)
# print( next(it) )
# print( next(it) )
# print( next(it) )

# for i in range(10,20,0.5):
#     print(i)

# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# for i in frange(10,20,0.5):
#     print(i)

# def true(): return True

# lambda : True
# print(true())

# a = [1,2,3,4,5,6,7]
# print(list(filter(lambda x:x>2 , a)))

# a = [1,2,3]
# b = [1,2,3]
# print(list(map(lambda x:x+1, a)))
# print(list(map(lambda x,y:x+y, a,b)))

# from functools import reduce
# print(reduce(lambda x,y: x+y, [2,3,4], 1))

# print(zip((1,2,3),(4,5,6)))
# for i in zip((1,2,3),(4,5,6),(7,8,9),(10,11,12)):
#     print(i)


# dicta = {'a': 'aa', 'b':'bb'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))


def fun():
    a = 1
    b = 2
    return (a + b)

fun()

def sum(a):
    def add(b):
        return a+b
    return add

# sum1 = fun()
# sum2 = sum(2)
# print(sum2(3))
# print(type(sum1))
# print(type(sum2))
