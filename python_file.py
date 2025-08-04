# A Simple User Input Age Calculator!!!
# a user defined function
def age():
  current_yr = int(input("Enter the current Year : "))
  current_month = int(input("Enter the current month : "))

  yr_birth = int(input("Enter your Birth Year : "))
  month_birth = int(input("Enter your Birth month : "))

  year = current_yr-yr_birth
  month = current_month-month_birth

  if month < 0:                                   # if ur bday month not yet came! this will adjust ur DOB.
    year = year - 1
    month = month + 12

  print(f'your are {year} years & {month} month old')


age()
