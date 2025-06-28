dict1 = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'fruit': 'apple',
}

print(dict1)
# print(dict1.get('fruit'))  # won't throw error due to get, it will return none
# print(dict1.get('fruit', "Banana"))  # won't throw error due to get, it will return default value of Banana

# user2 = dict(name1='john')
# print(user2)

# print(dict1.items())
# dict2 = dict1.copy()
# print(dict2)
#
# dict1.clear()
# print(dict1)
# print(dict2)
# print(dict1.pop('fruit'))
# print(dict1)
print(dict1.update({'greet': "Nice"}))
print(dict1)
