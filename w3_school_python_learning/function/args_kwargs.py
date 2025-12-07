'''
Python *args and **kwargs

By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.
'''

def give_emp_detail(*args):
    for value in args:
        print(value)
    print('args > ', args )

give_emp_detail('vishal', 'kumar', 35, 'hyderabad', 'kondapur', 'lloyds', 'guggu_kaka', 'motuku_guggu_kaka', 'mota_billota')  



def give_emp_detail(*args):
    # print(type(args))
    # print(args[8])
    return list(args)

emp_detail = give_emp_detail('vishal', 'kumar', 35, 'hyderabad', 'kondapur', 'lloyds', 'guggu_kaka', 'motuku_guggu_kaka', 'mota_billota')    

print(emp_detail)



# def caculate_total(*args):
#     args = (3,4,12,190, 3, 20, 40, 500)
#     total = 0
#     for num in args:
#         total = total + num  # or total += num
    
#     return total

# print(caculate_total(3,4,12,190, 3, 20, 40, 500))
# print(caculate_total(50, 100, 50, 10, 20, 30))

'''
Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:

'''

# def child_info(**kwargs):
#     print(kwargs)

# child_info(fname='Vishal', lname='Kumar')



# def my_function(**myvar):
#   print("Type:", type(myvar))
#   print("Name:", myvar["name"])
#   print("Age:", myvar["age"])
#   print("All data:", myvar)

# my_function(name = "Guggu", age = 8, city = "Noodlespur")



def my_function(**myvar):
    for [key,value] in myvar.items():
        print(f"{key} -> {value}")

my_function(name = "Guggu", age = 8, city = "Noodlespur")
