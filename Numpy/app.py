import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array))
print(array.shape)

array_zeros = np.zeros((3, 4))
print(array_zeros)
array_ones = np.ones((3, 4), dtype=int)
print(array_ones)
array_full = np.full((3, 4), 5, dtype=int)
print(array_full)
array_random = np.random.random((3, 4))
print(array_random)
print(array_random[0, 0])
print(array_random[array_random > 0.3])
print(array_random > 0.2)
print(np.sum(array_random))
print(np.floor(array_random))
print(np.round(array_random))

first = np.array([1, 2, 3])
second = np.array([4, 5, 6])
print(first + second)
print(first + 2)
print(first * 2)  # [n*2 for n in first]
