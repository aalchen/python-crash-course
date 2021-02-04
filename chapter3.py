# Python Crash Course exercises
# by Eric Matthes
# Chapter 3 - Lists

#3-1 - Names

names = ['Candy', 'Jerome', 'Richard', 'Yan']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2 - Greetings
print("\nHello, " + names[0] + ". How's it poppin?")
print("Hello, " + names[1] + ". How's it poppin?")
print("Hello, " + names[2] + ". How's it poppin?")
print("Hello, " + names[3] + ". How's it poppin?")

#3-3 - List of Cheeses
cheeses = [
    'Dubliner', 'aged cheddar', 'gruyere', 'fresh mozzerella',
    'parmesan reggiano'
]

print("\n" + cheeses[0].title() + " is such a delightfully sweet cheese!")
print("I can't imagine not having " + cheeses[1] +
      " in the fridge at all times.")
print(cheeses[2].title() + " is quite a versatile cheese to use in cooking.")
print(
    "If only " + cheeses[3] +
    " wasn't so expensive, otherwise I would eat twenty balls of it each day.")
print("Having just a bit of " + cheeses[-1] +
      " really makes a big difference, even in the simplest of dishes.")

#3-4 - Guest List
dinner_guests = ["Jeff Bezos", "Elon Musk", "Genghis Khan"]
print("\nDear " + dinner_guests[0] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[1] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[2] +
      ", you have been invited to my dinner party!")

#3-5 - Changing guest list
print("\nUnfortunately, " + dinner_guests[2] +
      " is unable to make the dinner.")
dinner_guests[2] = "Colonel Sanders"
print("\nDear " + dinner_guests[0] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[1] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[2] +
      ", you have been invited to my dinner party!")

#3-6 - Bigger guest list
print(
    "\nWe have found a bigger dinner table, therefore we'll be able to invite more guests!"
)
dinner_guests.insert(0, "Ryan Gosling")
dinner_guests.insert(2, "Spongebob")
dinner_guests.append("Gordon Ramsay")
print("\nDear " + dinner_guests[0] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[1] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[2] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[3] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[4] +
      ", you have been invited to my dinner party!")
print("Dear " + dinner_guests[5] +
      ", you have been invited to my dinner party!")

#3-7 - Shrinking Guest List
print("\nUnfortunately, we can only invite two people for dinner.")
popped = dinner_guests.pop()
print(
    "\nSorry " + popped +
    ", but you will have to come another time!  There is no room for you tonight."
)
popped = dinner_guests.pop()
print(
    "Sorry " + popped +
    ", but you will have to come another time!  There is no room for you tonight."
)
popped = dinner_guests.pop()
print(
    "Sorry " + popped +
    ", but you will have to come another time!  There is no room for you tonight."
)
popped = dinner_guests.pop()
print(
    "Sorry " + popped +
    ", but you will have to come another time!  There is no room for you tonight."
)

print("\nThankfully, you are still invited " + dinner_guests[0] + "!")
print("Thankfully, you are still invited " + dinner_guests[1] + "!")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)

#3-8 - Seeing the world
locations = [
    "Singapore", "Russia", "South Korea", "Mexico", "Brazil", "Thailand",
    "Indonesia", "Portugal"
]
print("\nThese are countries that I want to visit!")
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#3-9 Dinner Guests
dinner_guests_orig = ["Jeff Bezos", "Elon Musk", "Genghis Khan"]
print(len(dinner_guests_orig))

#3-10 Wildcard list
chips = ["Salt and Vinegar", "Ketchup"]
print(chips[0].upper())
print("I really love " + chips[1].lower() + " flavoured chips!")
chips[1] = "Catsup"
chips.append("Jalapenos")
chips.insert(0, "All Dressed")
print(chips)
del chips[2]
print(chips)
popped = chips.pop()
print(popped)
print(chips)
chips.append("Dill")
print(popped)
popped = chips.pop(1)
print(chips)
chips.remove("Dill")
print(chips)
chips.append("Nacho Cheese")
chips.append("Original")
chips.append("BBQ")
print(chips)
print(len(chips))
chips.sort()
print(chips)
chips.sort(reverse=True)
print(chips)