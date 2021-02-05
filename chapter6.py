# Python Crash Course exercises
# by Eric Matthes
# Chapter 6 - Dictionaries

#6-1 - Person
my_person = {
    'first_name': 'Ryan',
    'last_name': 'Gosling',
    'age': 25,
    'city': 'Vancouver',
}
print('\nHere are the details:')
print(my_person['first_name'])
print(my_person['last_name'])
print(my_person['age'])
print(my_person['city'])

#6-2 - Fave nums
fave_nums = {
    'candy': 3,
    'yan': 5,
    'richard': 9,
    'jerome': 666,
    'kumi': 1,
}

print("\nFave colours:")
print("Candy's favourite colour is: " + str(fave_nums['candy']))
print("Yan's favourite colour is: " + str(fave_nums['yan']))
print("Richard's favourite colour is: " + str(fave_nums['richard']))
print("Jerome's favourite colour is: " + str(fave_nums['jerome']))
print("Kumi's favourite colour is: " + str(fave_nums['kumi']))

#6-3 - Glossary
definitions = {
    'gasterbeiter': 'guest worker in germany',
    'leitkultur': 'leading culture',
    'heimat': 'national pride of the homeland'
}

print('\nDefinitions:')
print("gasterbeiter : " + definitions['gasterbeiter'])
print("leitkultur : " + definitions['leitkultur'])
print("heimat : " + definitions['heimat'])

#6-4 - Glossary 2

print("\nLooped definitions:")
for defs in definitions.keys():
    print(defs + ": " + definitions[defs])

definitions['hanschuhschneeballwerfer'] = 'being a coward'
definitions['ohrwurm'] = 'ear worm'
definitions['fernweh'] = 'homesickness'
definitions['kummerspeck'] = 'emotional overeating'
definitions['kuddelmuddel'] = 'a kerfuffle'

print("\nLooped definitions 2:")
for defs in definitions.keys():
    print(defs + ": " + definitions[defs])

#6-5 - Rivers

rivers = {'nile': 'egypt', 'rhine': 'germany', 'amazon': 'brazil'}

for riv in rivers.keys():
    print("The " + riv.title() + " runs through the " + rivers[riv].title())

print('\nRivers:')
for riv in rivers.keys():
    print(riv.title())

print('\nCountries:')
for riv in rivers.keys():
    print(rivers[riv].title())

#6-6 - Languages

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

need_polling = ['jen', 'chris', 'ryan', 'phil']

for name in favorite_languages.keys():
    if name in need_polling:
        print("Thanks for doing the poll, " + name + "!")
    else:
        print("Pls complete the poll asap, " + name + " :(")

#6-7 - People; dictionary in array

my_person2 = {
    'first_name': 'James',
    'last_name': 'Currie',
    'age': 29,
    'city': 'London',
}
my_person3 = {
    'first_name': 'Song',
    'last_name': 'Joongki',
    'age': 31,
    'city': 'Seoul',
}

my_peeps = [my_person, my_person2, my_person3]

print("\nMy peeps:")
for peeps in my_peeps:
    print('\n')
    for key in peeps:
        print(key + ": " + str(peeps[key]))

#6-8 - Pets

pickles = {'kind': 'llama', 'owner': 'amy'}

bobo = {'kind': 'dog', 'owner': 'lillian'}

dino = {'kind': 'tortoise', 'owner': 'soph'}

my_pets = [pickles, bobo, dino]

print("\nMy pets:")

for pets in my_pets:
    print("\n")
    for p in pets.keys():
        print(p + " : " + pets[p])

#6-9 - Favourite places

favourite_places = {
    'amy': ['ischia', 'glasgow', 'krakow'],
    'jerome': ['shirakawago', 'matsushima'],
    'candy': ['taipei']
}

print("\nMy friends favourite places:")
for name in favourite_places.keys():
    print("\n")
    print(name.title() + " loves going to:")
    for location in favourite_places[name]:
        print(location.title())

#6-10 - Favourite numbers; arrays in dictionary

fave_nums2 = {
    'candy': [3, 4, 99],
    'yan': [5],
    'richard': [29, 31],
    'jerome': [666, 6666],
    'kumi': [1],
}

for names in fave_nums2:
    print("\n" + names.title() + "'s favourite number(s) are:")
    for num in fave_nums2[names]:
        print(num)

#6-11 - Cities; dictionary in dictionary

cities = {
    'budapest': {
        'country': 'hungary',
        'cool sites': 'hot springs',
        'yummy food': 'goulash'
    },
    'prague': {
        'country': 'czechia',
        'cool sites': 'clocktower',
        'yummy food': 'trdelnik'
    },
    'venezia': {
        'country': 'italy',
        'cool sites': 'canals',
        'yummy food': 'gelato & spritz!'
    }
}

for city, fact in cities.items():
    print("\nThe city is :" + city.title() + "\n")
    print(fact['country'])
    print(fact['cool sites'])
    print(fact['yummy food'])