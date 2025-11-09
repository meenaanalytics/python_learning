'''Dictionary (Dictionaries are used to store data values in key:value pairs.)'''

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "model": "Mustang",
#   "model": "Ferrarie",
#   "model": "Tata",
#   "brand": "Ford",
#   "year": 1964,
#   "model": "Maruti",
# }

# thisdict["brand"] = 'BMW'
 
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict['model'])

# print(len(thisdict))


# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"],
#   "customer_detail" : {
#       'name': 'Vishal',
#       'Loan_info': 400000,
#       'customer_address': 'kartarpur',
#       'spouse_info': {
#           'spouse_name': 'Guggu',
#           'nick_name': 'suggu',
#           'hobby': 'tutu krna',
#       },
#   },
#   "brands": ('BMW', 'TATA', 'Maruti', 'Fortunier', 'Mercedes'),
#   "buying_history": {'12feb', '5june' , '45december', '35feb', '170march'}
# }

# print(thisdict['customer_detail'])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(type(thisdict))

# fruits = list(('apple', 'banana', 'cherry'))
# fruits = tuple(('apple', 'banana', 'cherry'))
# fruits = set(('apple', 'banana', 'cherry'))

# thisDict = dict(name= 'john', age=36, country= 'France')
# print(thisDict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict["brand"]
# x = thisdict.get('brand')

# x = thisdict.keys()
# x = thisdict.values()

# print(x)


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change



# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }


# print(car.items()) # gives you this : [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(type(x)) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# if "Model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#   print('Its not present!!!')


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 2000

# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({'year': 3000})

# print(thisdict)


'''Add extra Key , value in dictionary'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["top_speed"] = 350
# thisdict["gear"] = 6
# thisdict["enginer_cc"] = 500

# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.update({"color": "red"})
# print(thisdict)




'''EXTRAS (not required now )'''


# def calculator(operation, x, y):
#     if operation == 'ADD':
#         return x + y
#     elif operation == 'SUB':
#         return x - y
#     elif operation == 'MUL':
#         return x * y
#     else:
#         return x / y

# print(calculator(operation='ADD',y=5 , x=10))
# print(calculator(operation='SUB',y=5 , x=10))
# print(calculator(operation='MUL',y=5 , x=10))
# print(calculator(operation='DIV',y=5 , x=10))


'bla bla bla !!!!'