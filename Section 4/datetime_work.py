'''

Use the DateTime module to get Current Date and Time, and save it to a variable. 
Then extract just the Full month name form that variable.

'''

import datetime

current_date = datetime.datetime.now()

print(current_date.strftime("%B"))


