"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# get arguments
# no arguments -> print calendar for current month (datetime)
# 1 argument = month. Return that month for the current year
# 2 arguments = month and year
# elif print statement with the format expected and exit program
def get_calendar():

  if len(sys.argv) > 3:
    print("Format expected is \"14_cal.py [month] [year]\" where [month] and [year] are integer values")
  else:
    try:
      date = datetime.now()
      month = date.month
      year = date.year
      if len(sys.argv) > 1:
        month = int(sys.argv[1])
      if len(sys.argv) > 2:
        year = int(sys.argv[2])
      
      
      print("\n" + calendar.month_name[month] + ", " + str(year) + "\n")
      print(" S  M  T  W  T  F  S")
      print("--------------------")

      cal = calendar.monthcalendar(year, month)
      for row in cal:
        output = ""
        for day in row:
          if day == 0:
            output += " - "
          else:
            output += str(day) + " " if day > 9 else " " + str(day) + " "
        print(output)
        
    except ValueError:
      print("Invalid argument(s) value(s). Format expected is \"14_cal.py [month] [year]\" where [month] and [year] are integer values")
    except IndexError:
      print("Invalid date passed")

get_calendar()