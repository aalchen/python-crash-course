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
quit_prompt += "\nEnter 'quit' to end the program...\n"

message = ""

print(quit_prompt)
while message != 'quit':
    message_sent = input(prompt + "...")
    print("\nThanks! We will add " + message_sent + " to your pizza.")
