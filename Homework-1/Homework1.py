"""Joseph Nguyen PSID: 1779987"""
# CIS 2348 Homework #1 #

print("Birthday Calculator")
print("Current day")
current_month = int(input("Month:"))
current_day = int(input("Day:"))
current_year = int(input("Year:"))
print("Birthday")
birth_month = int(input("Month:"))
birth_day = int(input("Day:"))
birth_year = int(input("Year:"))

age = current_year - birth_year
if birth_month == current_month and birth_day == current_day:
    age = current_year - birth_year
    print("Happy birthday!")
if birth_month > current_month and birth_day > current_day:
    age = age - 1
if birth_month <= current_month and birth_day <= current_day:
    age = current_year - birth_year

print("You are", age, "years old.")
