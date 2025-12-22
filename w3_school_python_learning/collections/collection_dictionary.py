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


'''Remove Items'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   'color': 'Red'
# }

# thisdict.pop('brand')  # Remove mentioned Key:value
# thisdict.popitem()  # remove last inserted Key:value
# del thisdict['color']
# del thisdict

# thisdict.clear()  #empty the dictionary

# print(thisdict)

'''Loop over dictionary'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'color': 'Red'
}

print(thisdict['brand'])

for key_value in thisdict:
    print(thisdict[key_value])

x = 'brand'

print(thisdict[x])

for key in thisdict:
    print(f'{key} : {thisdict[key]}')


# for value in thisdict.values():
#     print(value)

# print(thisdict.keys())

# for key in thisdict.keys():
#   print(key)

# key_value_pair = thisdict.items()

# for key,value in key_value_pair:
#     print(f'{key}: {value}')


'''copy of dictionary'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# mydict['brand'] = 'Tata'

# print(mydict)
# print(thisdict)

# mydict = dict(thisdict)
# print(mydict)

'''Nested Dictionary'''

# child1 = {
#   "name" : "Ram",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Sham",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Ghanshyam",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily['child2']['name'])
# print(myfamily.values())

# for key,value in myfamily.items():
#     # print(f'{key}: {value}')
#     for inner_key, inner_value in value.items():
#         print(f'{inner_key}: {inner_value}')
    
#     print('--------------------------------')

