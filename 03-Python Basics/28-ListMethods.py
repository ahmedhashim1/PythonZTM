# fruits = ['apple', 'banana']
# fruits.append('orange')
# print(fruits)
# Output: ['apple', 'banana', 'orange']

# fruits = ['apple', 'banana']
# fruits.extend(['grape', 'mango'])
# print(fruits)
# Output: ['apple', 'banana', 'grape', 'mango']

# fruits = ['apple', 'banana']
# fruits.insert(1, 'kiwi')
# print(fruits)
# Output: ['apple', 'kiwi', 'banana']

# fruits = ['apple', 'banana', 'apple']
# fruits.remove('apple')
# print(fruits)
# # Output: ['banana', 'apple']

# fruits = ['apple', 'banana', 'orange']
# item = fruits.pop(1)
# print(item)
# print(fruits)
# Output: 'banana'
#         ['apple', 'orange']


# fruits = ['apple', 'banana', 'orange']
# print(fruits.index('banana'))
# Output: 1


# numbers = [1, 2, 3, 2, 2, 4]
# print(numbers.count(2))
# Output: 3

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)
# Output: [1, 2, 3, 4]


# fruits = ['apple', 'banana', 'orange']
# fruits.reverse()
# print(fruits)
# Output: ['orange', 'banana', 'apple']

# fruits = ['apple', 'banana']
# new_fruits = fruits.copy()
# new_fruits.append('grape')
# print(fruits)
# print(new_fruits)
# Output: ['apple', 'banana']
#         ['apple', 'banana', 'grape']


# fruits = ['apple', 'banana']
# fruits.clear()
# print(fruits)
# Output: []
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d', 0, 4))
print(basket.sort())
print(basket)
