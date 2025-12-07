'''
Python For Loops:
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages,
and works more like an iterator method as found in other 
object-orientated programming languages.

With the for loop we can execute a set of statements, 
once for each item in a list, tuple, set etc.
'''

fruits = ["apple", "cherry", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)


# my_name = ["v", "i", "s", "h", "a","l"]

# for x in my_name:
#     print(x)


fruits = ["apple", "cherry", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)
#     if fruit == "banana":
#         break
    
# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)



'''
The range() Function
To loop through a set of code a specified number of times, 
we can use the range() function,

The range() function returns a sequence of numbers, 
starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
'''

# for x in range(2 , 10 , 4):# range(2 , 10 , 4)
#    print(x)                # range(starting , ending , 
# steps to skip)

# for x in range(6):
#     print(x)
# else:
#     print("finally finished")    


# for x in range(6):
#     if x== 3:break
#     print(x)
# else:
#     print("finally finished")    


# colors = ["red", "white", "grey","black","pink"]
# fruits = ruits = ["apple", "cherry", "banana", "mango"]
# cars = ["tata", "maruti", "ford", "kia"]

# for color in colors:
#     for fruit in fruits:
#         for car in cars:
#             print(f"color: {color} , fruit: {fruit}, car:{car} ")


'''
The pass Statement
for loops cannot be empty, but if you for some reason 
have a for loop 
with no content, put in the pass statement to 
avoid getting an error.
'''

for x in [0, 1, 2]:
  pass
