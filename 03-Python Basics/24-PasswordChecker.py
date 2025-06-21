user_name = input('Please enter your username: ')
password = input('Please enter your password: ')
pass_len = len(password)
pass_masked = '*' * pass_len

print(f'{user_name}, Your password {pass_masked} is {pass_len} characters long.')