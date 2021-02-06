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