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

# print(thisdict['customer_detail']['spouse_info'])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year" : "1964"
# }

# print(type(thisdict))


# fruits = list(("apple", "banana","cherry", "mango"))
# fruits = tuple(("apple", "banana", "cherry", "mango"))
# fruits = set(("apple", "banana", "cherry", "mango"))

# thisDict = dict(name= "jhon" , age=39, country= "france")
# print(thisDict)


# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965

# }


# x = thisdict["brand"]
# x = thisdict.get("brand")

# x = thisdict.keys()
# x = thisdict.values()

# print(x)

# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# x = car.keys()

# print(x)   #before the change

# car["color"] = "white"

# print(x)    #after the change


# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# x = car.values()
# print(x)    # before the change

# car["year"] = 2020
# print(x)    # after the change



# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }


# print(car.items())   #give you this :[('brand', 'ford'), ('model', 'mustang'), ('year', 1965)]




# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# x = car.items() # before the change
# print(x)

# car["brand"] = "kia"
# print(x)    # after the change

# print(type(x))



# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#     print("its not present!!!") 



# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }


# thisdict["year"] = 2020

# print(thisdict)



# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# thisdict.update({'year': 3000})

# print(thisdict)


'''add extar key , values in dictinoary'''

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# thisdict.update({'year': 3000})

# thisdict["top_speed"] = 350
# thisdict["gear"] = 6
# thisdict["enginer_cc"] = 500

# print(thisdict)




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965
# }

# thisdict.update({"color": "red"})
# print(thisdict)



'''EXTRA (not required now)'''

# def calculator(operation, x , y):
#     if operation == 'ADD' :
#         return x + y
#     elif operation == 'SUB' :
#         return x - y
#     elif operation == 'mul' :
#         return x * y
#     else:
#         return x / y
    

# print(calculator(operation='ADD' , y=5 , x=10))
# print(calculator(operation='SUB' , y=5 , x=10))
# print(calculator(operation='MUL' , y=5 , x=10))
# print(calculator(operation='DIV' , y=5 , x=10))
     
'''bla  bla bla!!!'''



'''remove items'''

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1965 ,
#     "color": "red"

# }

# thisdict.pop('brand')   # removed mentation key:value
# thisdict.popitem()      # remove last inserted key:value
# del thisdict['color']
# del thisdict
# thisdict.clear()        # empty the dictionary

# print(thisdict)

'''loop over dictionary'''


thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1965 ,
    "color": "red"

}

# print(thisdict['brand'])

# for key_value in thisdict:
#     print(thisdict[key_value])

# x = 'brand'

# print(thisdict[x])

# for key in thisdict:
#     print(f'{key} : {thisdict[key]}')


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

child1 = {
  "name" : "Ram",
  "year" : 2004
}
child2 = {
  "name" : "Sham",
  "year" : 2007
}
child3 = {
  "name" : "Ghanshyam",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily['child2']['name'])
print(myfamily.values())

for key,value in myfamily.items():
    print(f'{key}: {value}')
    for inner_key, inner_value in value.items():
        print(f'{inner_key}: {inner_value}')
    
    print('--------------------------------')

