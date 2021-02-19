# Python Crash Course exercises
# by Eric Matthes
# Chapter 7 - User input & while loops

#7-1 - Rental Car

message = input("What kind of rental car are you interested in? ")
print("Let me see if I can find you a " + message)

#7-2 - Restaurant seating

num_seats = input("\nHow many people are in your dinner group? ")
num_seats = int(num_seats)
if num_seats > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")

#7-3 - Multiples of ten

num_given = input("\nGive me a number! ")
num_given = int(num_given)

if num_given % 10 != 0:
    print("This is not a multiple of 10")
else:
    print("This is a multiple of 10")

#7-4 - Pizza toppings

prompt = "\nWhat toppings do you want on your pizza?"
quit_prompt = "\nEnter 'quit' to end the program...\n"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

#7-5 - Movie tickets

prompt = "\nWhat is your age?"
age = input(prompt)
age = int(age)

if age < 3:
    print("Your ticket is free!")
elif age < 12:
    print("Your ticket is $10")
else:
    print("Your ticket is $15")

#7-6 - Three exits

prompt = "What is your age?"
active = True

while active:
    age = input(prompt)
    if age != "quit":
        print("Your age is " + age + "!")
    else:
        active = False
        break

#7-7 - Infinity

x = 10

while x < 100:
    print("hi")

#7-8 - Deli

sandwich_orders = ["Meatball Sub", "Margherita", "Clubhouse", "Avocado Toast"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I have made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches are done!")

for sandwichf in finished_sandwiches:
    print("We have made the " + sandwichf)

#7-9 - No Pastrami

sandwich_orders = [
    "Meatball Sub", "Pastrami", "Margherita", "Clubhouse", "Pastrami",
    "Avocado Toast", "Pastrami"
]
finished_sandwiches = []

print("Sorry! We've run out of pastrami")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

for sandwich in sandwich_orders:
    print("I have made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches are done!")

for sandwichf in finished_sandwiches:
    print("We have made the " + sandwichf)

#7-10 - Dream Vacation

prompt0 = "What's your name? "
prompt = "What is your dream vacation?"
prompt2 = "Do you want the poll to continue?"
responses = {}
active = True

while True:
    name = input(prompt0)
    vacay = input(prompt)
    responses[name] = vacay
    cont = input(prompt2)
    if cont == "yes":
        active = True
    elif cont == "no":
        active = False
        for name, vacations in responses.items():
            print(name.title() + " wants to go to " + vacations.title())
        break
