import numpy as np

# arr = np.array([2, 3, 4])
#
# print(arr)
# print(arr.dtype)
#
# arr2 = np.array([1.2, 2.3, 3.4])
# print(arr2)
# print(arr2.dtype)
#
# print(arr + arr2)
#
# print(arr2 * 10)

# data = [[1, 2, 3], [4, 5, 6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

# print(np.zeros((10, 10, 10)))
# print(np.zeros((3, 5)))
# print(np.ones((4, 6)))
#
# print(np.empty((2, 3, 2)))


arr5 = np.arange(10)
arr5[5:8] = 10
print(arr5)

arr_slice = arr5[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
