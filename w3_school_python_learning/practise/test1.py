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


# num = [4 , 50, 42 , 16 ,2]

# def SumofList(numList):
    # print(numList)
#     total = 0
#     for number in numList:
#         total = total+ number

#     return total 

# v=SumofList(num)    

# print(v)



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



def addFruitTolist(count):
    fruits = []
    for i in range(count):
        fruit = input('Enter Fruit : ')
        fruits.append(fruit)

    return f'Your fruit bucket : {fruits}'

fruitBucket = addFruitTolist(2)
print(fruitBucket)



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

