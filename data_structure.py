# List
strs = ["h", "i"]
numbers = [1]*10
print(numbers)

two_dimentinal_list = [[1, 3], [2, 4]]
print(two_dimentinal_list)

list1 = list("hello")
list2 = list(range(12))
list3 = list2 + strs
print(list3)

#methode in list
letters = ["w", "o", "r", "l", "d"]
print(letters[::2])

#packing, unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)
print(middle)
print(last)

for index, value in enumerate(numbers):
    print(index, value)

# List methodes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

numbers.sort(reverse=True)  # orginal list sorted
sorted(numbers)  # return sorted list
print(numbers)
numbers.pop(0)
numbers.pop()
print(numbers)
numbers.insert(0, 10)
del numbers[1: 3]
print(numbers)
numbers.clear()

items = [
    ("product1", 123),
    ("product2", 12),
    ("product3", 1)
]
items.sort(key=lambda item: item[1])
print(items)

# map function
x = list(map(lambda item: item[1], items))
print(x)
print([item[1] for item in items])


# filter function
y = list(filter(lambda item: item[1] < 10, items))
print(y)
print([item for item in items if item[1] < 10])
# comprehensions
# [expression for item in items]

# zip function
list1 = [1, 2, 3]
list2 = [100, 101, 103]
print(list(zip("abc", list1, list2)))


# stacks
# queues
# tuples
# swaping variables
# array
# set
# dictionary
# unpack and packing


sentenion = "this is the common interview question"

temp = {}
for character in sentenion:
    if character in temp:
        temp[character] = temp[character] + 1
        continue
    temp[character] = 1
print(temp)

string = max(temp.values())
print(list(filter(lambda z: temp[z] == string, temp))[0])
