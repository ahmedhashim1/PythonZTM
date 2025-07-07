# Error Handling
while True:
    try:
        age = int(input("What is your age?"))
        print(age)
        10 / age
    except ValueError:
        print("Sorry, only numbers allowed")
    except ZeroDivisionError:
        print("Age should be higher then 0.")
    else:
        print("Thank you for your time")
        break
