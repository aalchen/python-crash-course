# Python Crash Course exercises
# by Eric Matthes
# Chapter 8 - Functions

# #8-1 - Message
# def display_message():
#     print("I'm learning about functions in this chapter!")

# display_message()

# #8-2 - Favorite book
# def favorite_book(title):
#     print("One of my favourite books is " + title)

# favorite_book("Perilous Kinship")

# #8-3 - T-shirt
# def make_shirt(size, text):
#     print("Your shirt is size " + size.upper() + " and the message says " +
#           text)

# #Positional arguments
# make_shirt("m", "Bing Bang Bong")

# #Keyword arguments
# make_shirt(text="Ding Dang Dong", size="L")

# #8-4 - Large t-shirts
# def make_shirt(size="L", text="I love Python"):
#     print("Your shirt is size " + size.upper() + " and the message says " +
#           text)

# make_shirt()
# make_shirt("M")
# make_shirt(text="Hi")

# #8-5 - Cities
# def describe_city(city, country="Canada"):
#     print(city.title() + " is in " + country.title() + ".")

# describe_city("Toronto")
# describe_city("Vancouver")
# describe_city("Mannheim", "Germany")

# #8-6 - City Names
# def city_country(city, country):
#     print(city.title() + ", " + country.title())

# city_country("prague", "czech")
# city_country("ischia", "italy")
# city_country("glasgow", "scotland")

# #8-7 - Album
# def make_album(artist, album, num=""):
#     album = {'artist': artist, 'album': album, 'number': num}
#     return album

# album_info = make_album("Taylor Swift", "1989")
# print(album_info)

# #8-8 - While loop for User Albums
# active = True
# prompt1 = "What is the artist?"
# prompt2 = "What is the album?"
# prompt3 = "What is the number of tracks (optional)?"

# def make_album(artist, album, num=""):
#     album = {'artist': artist, 'album': album, 'number': num}
#     return album

# while active:
#     artist = input(prompt1)
#     album = input(prompt2)
#     num = input(prompt3)
#     if artist != "quit" or album != "quit" or num != "quit":
#         album_info = make_album(artist, album, num)
#         print(album_info)
#     else:
#         active = False
#         break

# #8-9 - Magicians

# magicians = ["ryan", "job", "michael", "tobias"]

# def show_magicians(magicians):
#     for mag in magicians:
#         print(mag)

# show_magicians(magicians)

# #8-10/11 - Great Magicians

# def make_great(magicians):
#     great_magicians = []
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + " the Great"
#         great_magicians.append(great_magician)
#     for great_magician in great_magicians:
#         magicians.append(great_magician)

# show_magicians(magicians)

# print("\n")
# make_great(magicians)
# show_magicians(magicians)

#8-12 - Sandwiches


def make_sandwich(*toppings):
    print(toppings)


make_sandwich("Lettuce", "Salami", "Cheddar")
make_sandwich("Arugula", "Proscuitto")
