# def AddTwoNum():
#     x = int(input("Enter first  number: "))
#     y = int(input("Enter second  number: "))
#     return x + y

# i=AddTwoNum()

# print(i)



# def AddThreeNum(num):
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
#     return x + y + num

# i=AddThreeNum(4) 

# print(i)


num = [4 , 50, 42 , 16 ,2]

def SumofList(numList):
    # print(numList)
    total = 0
    for number in numList:
        total = total+ number

    return total 

v=SumofList(num)    

print(v)



# def StrinLength(str1):
#     length = len(str1)
#     print(length)
#     return length

# name = 'vishal'
# StrinLength(name)



# fruits = ['apple', 'grapes', 'mango', 'cherry'] 

# def LengthString(fruitlist):
#     length = len(fruitlist)
#     return length

# z=LengthString(fruits)

# print(z)



# def addFruitTolist(count):
#     fruits = []
#     for i in range(count):
#         fruit = input('Enter Fruit : ')
#         fruits.append(fruit)

#     return f'Your fruit bucket : {fruits}'

# fruitBucket = addFruitTolist(2)
# print(fruitBucket)




# def addFruitTolist():
#     fruits = []
#     i = 0
#     j = 5
#     while i < j:
#         fruit = input("Enter fruits : ")
#         fruits.append(fruit)
#         i += 1

#     return f"Your fruit buckit: {fruits}"
    
# fruitBucket=addFruitTolist()

# print(fruitBucket)



'''
Write a function which take 2 list as a argument
list1 = ['name', 'age', 'city', 'salary']
list2 = ['Vishal', 34, 'Hyderabad', 50000]

employee_detail = {
'name':'Vishal',
'age': 34,
'city': 'Hyderabad',
'salary': 50000
}

return employee_detail
'''

# list1 = ['name', 'age', 'city', 'salary']
# list2 = ['Vishal', 34, 'Hyderabad', 50000]

# def aDDtOlisT(list1 , list2):
    
#     employee_detail = {}

#     for i in range(len(list1)):
#         # employee_detail[list1[i]] = list2[i]
#         key = list1[i]
#         value = list2[i]
#         employee_detail[key] = value


#     return employee_detail


# x = aDDtOlisT(list1,list2)
# print(x)


# list1 = ['name', 'age', 'city', 'salary']
# list2 = ['Vishal', 34, 'Hyderabad', 50000]

# def Employ_Details_while(list1 , list2):

#     obj = {}
#     i = 0
#     j = len(list1)

#     while i < j:
#         key = list1[i]
#         value = list2[i]
#         obj[key] = value
#         i += 1

#     return obj

# employ = Employ_Details_while(list1 , list2)

# print(employ)





# obj = {}

# obj['name'] = 'Vishal'
# obj['class'] = '10th'
# obj['grade'] = 'G'
# print(obj)

# ---------------helper-----------------
# obj = {
#     'adhar_number': '807134983',
#     'contact_number': '+919382233384',
#     'age': 32
# }

# aadhar_user_keys = []
# aadhar_user_values = []

# aadhar_user_keys.append(list(obj.keys())[0])
# aadhar_user_values.append(list(obj.values())[0])

# print(aadhar_user_keys)
# print(aadhar_user_values)

# for key,value in obj.items():
#     print(key, value)

# ---------------helper-----------------


Student_details_dict = {
    'Name' : 'Vishal',
    'Class' : '10th',
    'Subject' : 'Math',
    'Grade' : 'A'
}    

# {
#     'list1' : ['Name', 'Class', 'Subject', 'Grade'],
#     'list2' : ['Vishal', '10th', 'Math', 'A']
# }

# def Student_details(shi_link):
#     list1 = []
#     list2 = []

#     for key,value in shi_link.items():
#         list1.append(key)
#         list2.append(value)

#     return {
#         'list1': list1,
#         'list2': list2
#     }


# print(Student_details(Student_details_dict))



# def Student_details(dict1):
#     list1 = []
#     list2 = []

#     keys = list(dict1.keys())
#     values = list(dict1.values())

#     i = 0
#     j = len(keys)

#     while i < j:
#         list1.append(keys[i])
#         list2.append(values[i])
#         i += 1

#     return {
#         'list1': list1,
#         'list2': list2
#     }

# result = Student_details(Student_details_dict)
# print(result)





employee_detail = {
'name':'Vishal',
'age': 34,
'city': 'Hyderabad',
'salary': 50000
}

# 1.create a function which take dictionary as a argument
# 2.


# def generateEmployeeDetailLists(obj):
#     keysList = list(obj.keys())
#     valuesList = list(obj.values())

#     output = {
#         'list1': keysList,
#         'list2': valuesList
#     }

#     return output

# x = generateEmployeeDetailLists(employee_detail)
# print(x)

# def employee_detail(dict):
#     list1 = []
#     list2 = []

#     i = 0
#     j = len[key]

#     while i < j:
#         list1 key.append() 
#         list2 vale.append()

#     return {
#         'list1' = list1[i]
#         list2 = list2[i]
#     }

# x = employee_detail(employee_detaia)

# i = 0
# # j = 5

# while i < 5:
#     i +=1
#     print("Hello world")


# for i in range(5):

#     print("Hello world")

 
# i = 0
# j = int(input('Enter number: '))

# while i < j:
#     i +=1
#     print("Hello world")


# fruits = []

# hints
# len(fruits)
# print(fruit[i])


# fruits = ["apple", "cherry", "grapes", "lichi"]

# i = 0
# j = 5

# while i <j:
#     a = input("Enter a fruits : ")
#     fruits.append(a)
#     i += 1


# print(a) 
# #   

# fruits = ["apple", "cherry", "grapes", "lichi"]

# i = 0
# j = len(fruits)

# while i < j:
#     print(fruits[i])

#     i +=1



# fruits.reverse()
# i = 0
# j = len(fruits) # = 4

# while j > i: # 0 > 0
#     print(fruits[j - 1])
#     j -= 1 # j = 3



# fruits = ["apple", "cherry", "grapes", "lichi","mango","papaya","banana","guava","melon","watermelon"]
# fruits2 = []

# i = 0
# j = len(fruits)

# while i < j:
#     fruits2.append(fruits[i])
#     i +=1

# print(fruits2)



# Table of 2

# i = 1
# j = 11

# while i < j:
#     print(f"2 * {i} : {2 * i}")
#     i += 1



# a = int(input("Enter a number : "))
# table = []
# i = 1
# j = 11

# while i < j:
#     table.append(13 * i)
#     print(f"{a} * {i} : {a * i}")
#     i +=1

    