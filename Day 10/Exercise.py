''' Exercise 1 - Days in Month '''

def is_leap(year):
  """Takes in a year as input and returns whether True or False,
  depending on if input is a leap year."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year_to_check, month_to_check):
    if (month_to_check < 1) and (month_to_check > 12):
        return "Invalid input." 
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year_to_check):
        month_days[1] = 29
    return month_days[month_to_check-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year_to_check=year, month_to_check=month)
print(days)
print()








