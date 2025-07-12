from collections import Counter, defaultdict, OrderedDict

# Counter
li = [1, 2, 3, 4, 5, 6, 7, 7]
# print(Counter(li))

sent = "Thinking about python"
# print(Counter(sent))

# Default Dictionary
dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
# print(dict['c'])  # it will return zero instead of error

# Ordered Dictionary
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)  # will return true if order of insertion is same, false otherwise
