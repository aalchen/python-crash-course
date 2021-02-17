# Python Crash Course exercises
# by Eric Matthes
# Chapter 5 - If statements

#5-1 - Conditionals
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5-2 - More Conditionals
print('gruyere' == 'GRUYERE')
print('gruyere'.upper() == 'GRUYERE')
print(3 >= 0)
print(3 >= 2)
print(3 >= 3)
print(3 >= 4)
print(3 > 2 and 1 > 2)
print(3 > 2 or 1 > 2)

checkList = ['gruyere', 'cheddar', 'mozzy']
cheese = 'gruyere'
cheese2 = 'havarti'

print(cheese in checkList)
print(cheese2 in checkList)

#5-3 - Alien colours

colour1 = "green"
colour2 = "blue"

if colour1 == "green":
    print("You've won 5 points!")

if colour2 == "green":
    print("You've won 5 points!")

#5-4 - Alien colours 2

if colour1 == "green":
    print("You've won 5 points!")
else:
    print("You've won 10 points!")

if colour2 == "green":
    print("You've won 5 points!")
else:
    print("You've won 10 points!")

#5-5 - Alien colors 3

colour1 = "green"
colour2 = "yellow"
colour3 = "red"

if colour1 == "green":
    print("You've won 5 points!")
elif colour1 == "yellow":
    print("You've won 10 points!")
elif colour1 == "red":
    print("You've won 15 points!")

if colour2 == "green":
    print("You've won 5 points!")
elif colour2 == "yellow":
    print("You've won 10 points!")
elif colour2 == "red":
    print("You've won 15 points!")

if colour3 == "green":
    print("You've won 5 points!")
elif colour3 == "yellow":
    print("You've won 10 points!")
elif colour3 == "red":
    print("You've won 15 points!")

#5-6 - Stages of life

age = 1

if age < 2:
    print("you a baby")
elif age < 4:
    print("you're a toddler")
elif age < 13:
    print("you're a kiddo")
elif age < 20:
    print("you're a teen")
elif age < 65:
    print("you're an adult")
elif age >= 65:
    print("you're an old person damn")

#5-7 Favourite fruit

fave_fruits = ["watermelon", "nectarine", "grapes"]
check_fruit = "watermelon"

for fruit in fave_fruits:
    if fruit == check_fruit:
        print("You really like " + fruit)

#5-8 - Hello Admin

usernames = ["admin", "amy", "chris", "kyle", "allyson"]
user = "admin"
for un in usernames:
    if un == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + un + ", thanks for logging in again!")

#5-9 - No users

usernames2 = []

if usernames2:
    for un in usernames2:
        print("Logging in!")
    print("Done")
else:
    print("This is empty.")

#5-10 - Checking unique usernames

curr_usernames = ["admin", "amy", "chris", "kyle", "allyson"]
new_usernames = ["amy", "yan", "jerome", "kyle", "trixie", "ALLYSON"]

curr_usernames_lower = [user.lower() for user in curr_usernames]

for new in new_usernames:
    if new.lower() in curr_usernames_lower:
        print("Please add a new username. The username " + new +
              " already exists.")
    else:
        print("This username " + new + " is available.")

#5-11 - Ordinal numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 1:
        print("1st\n")
    elif num == 2:
        print("2nd\n")
    elif num == 3:
        print("3rd\n")
    else:
        print(str(num) + "th\n")