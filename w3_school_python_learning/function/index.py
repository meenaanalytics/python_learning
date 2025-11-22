'''function

Python Functions

A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.

'''

# def chole_bhature():
#     print('I Love Chole Bhature')


# for x in range(100):
#     chole_bhature()


# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)



# def fahrenheit_to_celsius(temp):
#     cel = (temp - 32) * 5 / 9
#     return round(cel, 2)
   

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

# my_temprature = [34, 12, 124, 56 , 87, 34 , 12 , 34 , 56 , 78 ,86, 32, 56 ,87, 90]

# for temprature in my_temprature:
#     print(fahrenheit_to_celsius(temprature))

# def myFunc():
#     pass

# emp_info: {
#     "name": "vishal",
#     "age" : "35",
#     "exp.": "5"
# }

# def give_emp_details():
#     key = ["name", "age", "exp."] 
#     value = ["Vishal", "35", "5"]

#     # key[0]

#     emp_info = {}

#     # emp_info['name'] = 'Vishal'

#     for i in range(len(key)): #range(len(key)) -> range(3)
#         # print('inside for loop > ', i)
#         emp_info[key[i]] = value[i]
    
#     return emp_info
       

# emp_data = give_emp_details()
# emp_data2 = give_emp_details()

# print(emp_data)
# print(emp_data2)


'''
Arguments:
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

'''

# value = ["Vishal", "35", "5"]

# def give_emp_details(value):
    # key = ["name", "age", "exp."] 
    # emp_info = {}

    # for i in range(len(key)):
    #     emp_info[key[i]] = value[i]
    
    # return emp_info
    
# emp_detail = give_emp_details( 
#     ["Vishal", "35", "5"]
#     )
# emp_detail2 = give_emp_details( 
#     ["Rohan", "55", "20"]
#     )
# emp_detail3 = give_emp_details( 
#     ["Rohit", "550", "200"]
#     )
# print(emp_detail)
# print(emp_detail2)
# print(emp_detail3)


'''
Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

🚨A parameter is the variable listed inside the parentheses in the function definition.

🚨An argument is the actual value that is sent to the function when it is called.
'''

'''How many argument function can take ?'''
'''A function can take n(jinna marji) number arguments'''

# def userDetail(
#         username='Ram', 
#         password='test123', 
#         age='28', 
#         isHealthy='False', 
#         Profession='Cook', 
#         salary=40000, 
#         city='Tokyo'):
#     print(username, password, age, isHealthy, Profession, salary, city)

# userDetail('Rohan','1123', '35', True,'Driver', 35000, 'Torronto')
# userDetail('Rohan','1123', '35', True,'Driver', 35000)
# userDetail()


# def my_function(fname, Lname):
#   print(fname + " " + Lname)

# my_function(name = "Buddy", animal = "dog",)
# my_function(Lname="Kumar", fname="Vishal")
# my_function("Kumar", "Vishal")


# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", age = 5, name = "Buddy")



# def my_function(person):
#   print("Name:", person["name"])
#   print("Age:", person["age"])

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)

# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)

# def my_function():
#   return ["apple", "banana", "cherry"]

# fruits = my_function()
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])




# def my_function():
#   return (10, 20)

# my_tpl = my_function()
# print("x:", my_tpl[0])
# print("y:", my_tpl[1])

# x, y = my_function()
# print("x:", x)
# print("y:", y)



'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add , / after the arguments:
'''

# def my_function(name, /): # '/'  then it will only expect positional argument
#   print("Hello", name)

# my_function("Ram")


'''
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
Example:
'''

# def my_function(*, name): # '*' only accept keyword arguments
#   print("Hello", name)

# my_function(name = "Emil")





# def my_function(a, b, /, *, c, d):
#   return a + b + c + d

# result = my_function(5, 10, c = 15, d = 20)
# print(result)
