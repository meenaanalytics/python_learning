# name = 'Vishal'
# job = 'software engineer'
# location = 'Hyderabad'

'''Many Values to Multiple Variables'''

# name , job, location = 'Vishal', 'Software engineer', 'Hyderabad'

# print('Details : ', {name, job, location})

'''One Value to Multiple Variables'''

# x = 5
# y = 5
# z = 5

# x = y = z = 5
# print(f"x: {x}, y:{y}, z:{z}")
# print(x,y,z)

'''Unpack a Collection'''

# fruits = ["apple", "banana", "cherry"]
# fruits = ("apple", "banana", "cherry")

# for fruit in fruits:
#     print(fruit)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# fruit1, fruit2, fruit3 = fruits

# print(fruit1, fruit2, fruit3)

'''string concatination'''  #string + string ( 'vish' + 'al' = 'vishal')

x = "Guggu "
y = "is "
z = "buutifuul"
# a = x + y + z
a = f'x:{x} y:{y} z:{z}'

print(a)
