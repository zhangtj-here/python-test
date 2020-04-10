# j = 123
# i = j

# print()

# a = '123'
# print(a[3])

# d = {'a': 1, 'b': 2}
# print(d['c'])

# year = int(input('input year:'))

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('aaa')
# print(1/'a')
# except (ValueError, AttributeError, KeyError)
try:
    print(1/0)
except ZeroDivisionError as e:
    print('0不能作为除数 %s' %e)

# try:
#     print(1/'a')
# except Exception as e:
#     print('123 %s' %e)

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')


# try:
#     a = open('name8.txt')
# except Exception as e:
#     print(e)
#
# finally:
#     a.close()
