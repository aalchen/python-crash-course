# Python Crash Course exercises
# by Eric Matthes
# Chapter 2 - Variables and Simple Data Types

#2-1 - Variable
message = "hello world"
print(message.title())

#2-2 - Variable re-assignment
message2 = "hello world"
print(message2)
message2 = message2.title() + "!"
print(message2)

#2-3 - Personal message
name = "amy"
message3 = "Hello " + name.title(
) + ", do you want to learn some Python today?"
print(message3)

#2-4 - Name cases
print(name.lower())
print(name.upper())
print(name.title())

#2-5 - Quotes
print(
    '\tFrank Reynolds once said, "Can I offer you an egg in this trying time?"'
)

#2-6 - Quotes broken down
famous_person = "Frank Reynolds"
message = '\t' + famous_person + ' once said, "Can I offer you an egg in this trying time?"'
print(message)

#2-7 - Stripping names
name2 = "\t      Ryan \n \t Gosling    "
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

#2-8 - Number 8
print(5 + 3)
print(2**3)
print(80 / 10)
print(4.2 + 3.8)
print(2 * 4)
print(10 - 2)
print(5 * 2 - 2)

#2-9 - Favourite number
fav_num = 85
print("My favourite number is " + str(fav_num) + ".")

#2-10 - Comments
# Hi, this is a comment!

#2-11 - Zen of Python
import this