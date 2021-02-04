# Python Crash Course exercises
# by Eric Matthes
# Chapter 4 - Working with lists

#4-1 - Pizza List
pizzas = ["Hawaiian", "Margherita", "Mushroom"]
print("Basic loop:")
for pizza in pizzas:
    print(pizza)
print("\nLoop in sentence:")
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
    print(pizza + " really is the best.")

print("\nI love pizza so much....")

#4-2 - Animal List
fuzzy_animal = ["cat", "dog", "bunny", "alpaca"]
for animal in fuzzy_animal:
    print(animal)
print("\nLoop in sentence:")
for animal in fuzzy_animal:
    print("My friend has a " + animal + " that is super cute!")

print("I'd love to own one of these animals one day!")

#4-3 - Counting to 20
printing = range(1, 21)
for number in printing:
    print(number)

#4-4 - Counting to 1M
printing_1m = range(1, 1000001)
# for number in printing_1m:
#     print(number)

#4-5 - Checking 1M
print("\nThe min is " + str(min(printing_1m)))
print("The max is " + str(max(printing_1m)))
print("The sum is " + str(sum(printing_1m)))

#4-6 Odd numbers
printing_odd = range(1, 21, 2)
for number in printing_odd:
    print(number)

#4-7 Threes
printing_threes = range(3, 31)
for value in printing_threes:
    print(value * 3)

#4-8 Cubes
printing_cubes = range(1, 11)
for value in printing_cubes:
    print(value**3)

#4-9 Cube comprehension
printing_cubes_comp = [value**3 for value in range(1, 11)]
print(printing_cubes_comp)

#4-10 Slices

print("\nThe first 3 items in my list are : ")
for animal in fuzzy_animal[:3]:
    print(animal)

fuzzy_animal.append("hamster")

print("\nThe middle 3 items in my list are : ")
for animal in fuzzy_animal[1:4]:
    print(animal)

print("\nThe last 3 items in my list are : ")
for animal in fuzzy_animal[2:5]:
    print(animal)

#4-11 - My pizzas, your pizzas
friend_pizzas = pizzas[:]

friend_pizzas.append("Cheese")

print("\nMy favourite foods are : ")
print(pizzas)

print("\nMy friend's favourite foods are : ")
print(friend_pizzas)

print("\nLoop version!")

print("\nMy favourite foods are : ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite foods are : ")
for pizza in friend_pizzas:
    print(pizza)

#4-13 - Buffet
basic_foods = ("roast beef", "chicken wings", "mussels", "bad sushi",
               "french fries")
print("\nBuffet foods:")
for food in basic_foods:
    print(food)

basic_foods = ("mac n cheese", "chicken wings", "mussels", "fried rice",
               "french fries")
print("\nUpdated Buffet foods:")

for food in basic_foods:
    print(food)

#4-14 - Checked PEP 8!

#4-15 - Completed code review!
