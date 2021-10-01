#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current year is: %Y")) #Takes a string argument and interprets the codes we pass in
  print(now.strftime("%a, %d, %B %y")) #formating string

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("locale date and time: %c"))
  print(now.strftime("locale date: %x"))
  print(now.strftime("locale time: %X"))
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("current time: %I:%M:%S %p"))
  print(now.strftime("24-hr time: %H:%M"))

if __name__ == "__main__":
  main();
