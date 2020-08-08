import calendar

user_input = input("Please enter a date in format of 'dd/mm/yyyy': ")
day = int(user_input[:2])
month = int(user_input[3:5])
year = int(user_input[6:])
print(calendar.day_name[calendar.weekday(year, month, day)])

"""
GET DATE BY THE USER AND PRINTING BACK WHICH DAY WAS THIS DATE
"""
