'''
The *try* block lets you test a block of code for errors.

The *except* block lets you handle the error.

The *else* block lets you execute code when there is no error.

The *finally* block lets you execute code, regardless of the result of the try- and except blocks.

'''

# print(x)

# x = 50

# try:
#   print(x)
# except:
#   print("x define hni ji!")


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


'''
You can use the else keyword to define a block of code to be executed if no errors were raised:
'''

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")



'''
The finally block, if specified, will be executed regardless if the try block raises an error or not.
'''

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")



# import os

# # Get Python file directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Build file path inside that directory
# file_path = os.path.join(current_dir, "demofile.txt")


# try:
#   f = open(file_path, 'a+')
#   try:
#     name = input('Enter something to put in File: ')
#     f.write(name)
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


'''
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

'''

# x = -1

# try:
#     if x < 0:
#         raise Exception("Sorry, no numbers below zero")
# except Exception as a:
#     print(a)
# except:
#     print('Error aa gya!')


# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

