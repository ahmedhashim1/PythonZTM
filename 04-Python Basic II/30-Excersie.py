# given the function to return highest Even number from the list
def highest_even(li):
    highest_even_num = None
    for num in li:
        if num % 2 == 0:  # Check if the number is even
            if highest_even_num is None or num > highest_even_num:
                highest_even_num = num
    return highest_even_num


my_list1 = [1, 2, 3, 4, 20, 6, 7, 8, 9, 10]
print(f"The highest even number in {my_list1} is: {highest_even(my_list1)}")
