'''
Write a block of code to handle one of the most common Python exception errors. 
Select one of the common errors from the curriculum section on Python Exception handling. 
Have your code example uses the try,except, else, and finally components.

'''


num = "Enter your number"

try:
    if(num > 25):
        print('number is greater than 25')
except TypeError:
    print("Error in data type")
else:
    print(type(num))
finally:
    print('finally block executed')
