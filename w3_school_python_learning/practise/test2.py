# i = 1
# j = 11

# while i < j:
#     print(f"3 * {i} : {3* i}")
#     i +=1



# def Tablesheet(table):

#     i = 0
#     j = 10


#     while j > i:
#         print(f"{table} * {j} : {table * j}")
#         j -=1

# Tablesheet(5)


# def tableTime(table , a , b):

#     for v in range(a , b):
#         print(f"{table} * {v} : {table * v}")

        
# tableTime(7 , 35 , 45)



# def tableTable(table , a , b):

#     for _ in range(a , b):
#         print(f"{table} * {_} : {table * _}")

#     print("----------------------------------")

#     i = a
#     j = b
#     while i < j:
#         print(f"{table} * {i} : {table * i}")
#         i +=1

# tableTable(3 , 1, 11)


# GUGGU
# BUDDU

def TabletAble(table , a , b , method):
    print('method >> ',method)

    if method == 'FOR':
        print('For loop block!!')
        for _ in range(a , b):
            print(f"{table} * {_} : {table * _}")
            
    else:
        print('While loop block!!')
        i = a
        j = b
        while i < j:
            print(f"{table} * {i} : {table * i}")
            i += 1


TabletAble(2 , 1 , 9 , "WHILE")




'''
** Home Work **
create one list at the top of function then push the output to that list and return it.
instead of printing table push table output to the list like : [2,4,6,8,10,...]
'''


# table = []

# def addtAbleList(count ):
#     table = []
#     for i in range(1, 11 ):
        
        
#         table.append(count * i)
        
#     return table

# x = addtAbleList(2)
# print(x)


# i = 1

# while i < 11:

#     table.append(* i)
#     i += 1

# return 


def TabletAble(table , a , b , way):
    output = []

    if way == 'FOR':
        print('For loop block!!')
        for _ in range(a , b):
            # print(f"{table} * {_} : {table * _}")
            output.append(table * _)
            
    else:
        print('While loop block!!')
        i = a
        j = b
        while i < j:
            # print(f"{table} * {i} : {table * i}")
            output.append(table * i)
            i += 1
    
    return output


callit = TabletAble(2 , 1 , 9 , "FOR")
print(callit)

