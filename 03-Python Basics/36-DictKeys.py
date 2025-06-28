dict2 = {
    123: [1, 2, 3],
    True: "hello",
    # [100]: True
}

# cannot use a hashable data type as a key

# print(dict2[123][0])

dict3 = {
    123: [1, 2, 3],
    123: [4, 5, 6],

    # [100]: True
}

# duplicate keys, python always pick the latest one
print(dict3[123])
