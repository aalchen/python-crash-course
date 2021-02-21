# Python Crash Course exercises
# by Eric Matthes
# Chapter 8 - Functions


#8-1 - Message
def display_message():
    print("I'm learning about functions in this chapter!")


display_message()


#8-2 - Favorite book
def favorite_book(title):
    print("One of my favourite books is " + title)


favorite_book("Perilous Kinship")


#8-3 - T-shirt
def make_shirt(size, text):
    print("Your shirt is size " + size.upper() + " and the message says " +
          text)


#Positional arguments
make_shirt("m", "Bing Bang Bong")

#Keyword arguments
make_shirt(text="Ding Dang Dong", size="L")


#8-4 - Large t-shirts
def make_shirt(size="L", text="I love Python"):
    print("Your shirt is size " + size.upper() + " and the message says " +
          text)


make_shirt()
make_shirt("M")
make_shirt(text="Hi")


#8-5 - Cities
def describe_city(city, country="Canada"):
    print(city.title() + " is in " + country.title() + ".")


describe_city("Toronto")
describe_city("Vancouver")
describe_city("Mannheim", "Germany")


#8-6 - City Names
def city_country(city, country):
    print(city.title() + ", " + country.title())


city_country("prague", "czech")
city_country("ischia", "italy")
city_country("glasgow", "scotland")