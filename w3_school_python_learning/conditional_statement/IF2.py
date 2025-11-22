'''Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.'''

# a = 33
# b = 400

# if b > a:
#     print("b is greater than a")


# number = 15
# if number >0:
#     print("the number is positive")


'''❌ Wrong indent , it will give error , ensure Indentation'''

# a = 33
# b = 200
# if b > a:
# print("b is greater than a")  # you will get an error



# age = 20
# if age >= 18:
#     print("you are an adult")
#     print("you can vote")
#     print("you have full legal rights")


# is_logged_in = True

# if is_logged_in:
#   print("Welcome back!")



'''The Elif Keyword

The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
'''


# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")



'''
How Elif Works:

When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.'''


# score = int(input('Enter your Score: '))

# if score >= 90:
#   print("Grade: A")
# elif score >= 80:
#   print("Grade: B")
# elif score >= 70:
#   print("Grade: C")
# elif score >= 60:
#   print("Grade: D")
# else:
#   print('Tata bye bye khatam gya!!!')


'''
When to Use Elif:

Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

'''


# day = int(input('Enter Day number : '))

# if day == 1:
#   print("Monday")
# elif day == 2:
#   print("Tuesday")
# elif day == 3:
#   print("Wednesday")
# elif day == 4:
#   print("Thursday")
# elif day == 5:
#   print("Friday")
# elif day == 6:
#   print("Saturday")
# elif day == 7:
#   print("Sunday")



'''
The Else Keyword:

The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.'''


# day = int(input('Enter Day number : '))

# if day == 1:
#   print("Monday")
# elif day == 2:
#   print("Tuesday")
# elif day == 3:
#   print("Wednesday")
# elif day == 4:
#   print("Thursday")
# elif day == 5:
#   print("Friday")
# elif day == 6:
#   print("Saturday")
# elif day == 7:
#   print("Sunday")
# else:
#   print('No day!!!')


# username = input('Enter your username: ')

# print('Length of username : ', len(username))

# if len(username) > 0: # 13 > 0
#   print(f"Welcome, {username}!")
# else:
#   print("Error: Username cannot be empty")




'''
Short Hand If :

If you have only one statement to execute, you can put it on the same line as the if statement.'''


# a = 5
# b = 2

# if a > b: print("a is greater than b")

# a = 2
# b = 330

# print("A") if a > b else print("B")

# a = 10
# b = 20

# bigger = a if a > b else b

# print("Bigger is", bigger)

# a = 330
# b = 330

# print("A") if a > b else print("=") if a == b else print("B")

# #    ⬆️
# # both are same
#     # ⬇️

# if a > b:
#     print("A")
# else:
#     if a == b:
#         print("=")
#     else:
#         print("B")



'''
 Python Logical Operators:
 Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true

'''
 


# a = 200
# b = 33
# c = 500

# if a > b and c > a:
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500

# if a > b or a > c:
#    print("At least one of the conditions is True")



# a = 33
# b = 200

# if not a > b:
#   print("a is NOT greater than b")
  



#   age = 25
# is_student = False
# has_discount_code = True

# if (age < 18 or age > 65) and not is_student or has_discount_code:
#   .            False.     and    True     or  True
#    .                              False     or  True
                                         #    True
#   print("Discount applies!")


# username = "Ram"
# password = "secret123"
# is_verified = True


# if username and password and is_verified:
#     #True   and   True  and True
#                 # True and True
#                 #     True
#   print("Login successful")
# else:
#   print("Login failed")


'''Nested If else'''

# username = "ram"
# password = "vishak143143//"
# is_active = True

# if username:
#     if password:
#         if is_active:
#             print("login successful")
#         else:
#             print("account is not active")
#     else:
#         print("password is requirde")
# else:
    # print("user name is required")


    


