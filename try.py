
try:
    #value = 10/0
    number = int(input("Enter a number: "))                  #Example of using code to print something on an error using [if, try, except, and other error metods]                                   
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input Error ")    