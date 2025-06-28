''' Write a simple function that takes 2 parameters -- a first name and a day name.

Set a default value for the day name of Sunday.

Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!".
 Remember to use the variables in the greeting to replace first-name and day-name.

Invoke this function with 2 variables.

Invoke this function with 1 variable only.'''

day_name = 'Sunday'

def func(first_name, day_name):
    print(f"Hi {first_name}! Happy {day_name}!")

func('Maria','Monday')
func('Maria')    #error

