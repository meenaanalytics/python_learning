import random

'''
normal user come to app.
App ask first name & last name
then ask for age 
then ask for phone number
then ask for address

print 'Student detail created' 
store all detail of student in a dictionary in a key value format
ask how much courses he want to avail.
ask student courses he want to avail max 5 , min 3
store this courses in the same student dictionary where
generate roll number of 10 character and store it into student obj
print monthly 100, yearly 1200
which category he want to select M/Y : 
store this category in student obj
now how much you want to pay 
print this is your pending balance which should be clear by 

'''


# {
#     'first_name': 'vishal', 
#     'last_name': 'kumar', 
#     'age': 45, 
#     'phone_number': '23089423094', 
#     'address': 'abc', 
#     'course_count': 4, 
#     'courses_list': ['science', 'english', 'biology', 'math']
# }

# student_dict = {}

# MIN_COURSE_COUNT = 3
# MAX_COURSE_COUNT = 5
# MONTHLY_FEES = 100
# YEARLY_FEES = 1200


# first_name = input('Enter you first name : ')
# last_name = input('Enter you last name : ')
# age = int(input('Enter your age : '))
# phone_number = input('Enter you phone number : ')
# address = input('Enter your address: ')

# student_dict['first_name'] = first_name
# student_dict['last_name'] = last_name
# student_dict['age'] = age
# student_dict['phone_number'] = phone_number
# student_dict['address'] = address

# print('Student details created in DB!!')


# course_count = int(input('How much courses you want to avail (min 3 , max 5 ) : '))

# if course_count > 5:
#     print('Maximum 5 courses per student is allowed!!')
# elif course_count < 3:
#     print('Minimum 3 courses required per student!! ')
# else:
#     student_dict['course_count'] = course_count

# courses_list = []

# for i in range(course_count):
#     course = input(f'Enter course name {i+1} : ')
#     courses_list.append(course)

# student_dict['courses_list'] = courses_list

# roll_number = random.randint(10**9, 10**10 - 1)

# student_dict['roll_number'] = roll_number

# print(f'Monthly fees : {MONTHLY_FEES} , Yearly: {YEARLY_FEES}')

#  fees_category = input('Which category you want to avail (Y for yearly , M for monthly) : ')

# student_dict['fees_category'] = fees_category

# currently_paid = int(input('How much you want to pay now : '))

# student_dict['currently_paid'] = currently_paid

# if student_dict['fees_category'] == 'M':
#     student_dict['pending_balance'] = MONTHLY_FEES - currently_paid
# else:
#     student_dict['pending_balance'] = YEARLY_FEES - currently_paid


# print(student_dict)

# print(f'Your pending balance is {student_dict['pending_balance']} , make sure to clear all dues before end of your category date')

'''-------------------------------------------------------------------------------------------'''


# import string

'''5️⃣ Hotel Booking System
Requirements:
Ask customer name, phone
Ask room type:
Single → ₹1000
Double → ₹2000
Ask number of days
Calculate total cost
Ask amount paid
Store pending amount
Generate booking ID
Store everything in dictionary'''

# booking_system = {}

# SINGLE_ROOM = 1000
# DOUBLE_ROOM = 2000


# customer_name = input("Enter your name : ")
# phone_number = int(input("Enter your phone number : "))

# booking_system['booking_system'] = booking_system
# booking_system['phone_number'] = phone_number


# room_type = input("Enter your room(S for single/D for double) : ")
# booking_system['room_type'] = room_type



# days = int(input("Enter how many days : "))
# booking_system['days'] = days


# if room_type == 'S':
#     total_cost = SINGLE_ROOM * days
# elif room_type == 'D':
#     total_cost = DOUBLE_ROOM * days
# else:
#     print("three sitter room is not avail")


# booking_system['total_cost'] = total_cost


# amount_paid = int(input("Enter amount paid : "))
# booking_system['amount_paid'] = amount_paid
# pending_amount = total_cost - amount_paid
# booking_system['pending_amount'] = pending_amount


# booking_id = "BK" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
# booking_system['booking_id'] = booking_id

# for key, value in booking_system.items():
#     print(f"{key} : {value}")

# print("Pending amount:", pending_amount)



'''---------------------------------------------------------------------------------'''


'''4️⃣ Password Strength Checker

Scenario:
Validate user passwords.
Requirements:
Check password rules:
Minimum 8 characters
At least 1 uppercase letter
At least 1 lowercase letter
At least 1 digit
At least 1 special character
Print why password is weak or strong'''


# def validateUserPassword(password):

#     ruleBook = {
#         'uppercase_letter' : False,
#         'lowercase_letter' : False,
#         'is_digit': False,
#         'is_special_character': False,
#     }

#     if password == '':
#         return "Password can't be empty"
#     else:
#         if len(password) >= 8:
#             for char in password:
#                 if char.isupper():
#                     ruleBook['uppercase_letter'] = True
#                 elif char.islower():
#                     ruleBook['lowercase_letter'] = True
#                 elif char.isdigit():
#                     ruleBook['is_digit'] = True
#                 else:
#                     ruleBook['is_special_character'] = True
            
#             for key,value in ruleBook.items():
#                 if value == False:
#                     return f'Atleast 1 {key} is required'
            
#             return 'Your password is Strong!!'
        
#         else:
#             return 'Please enter atleast 8 characters'


# passWord = input('Enter your password : ')
# result = validateUserPassword(passWord)
# print(result)



'''6️⃣ Mobile Recharge App
Requirements:

Ask user name, mobile number
Select recharge plan:

1 month → ₹199
3 months → ₹599
1 year → ₹1999

Store plan details
Ask payment amount
Print remaining balance or success message
Generate transaction ID'''

plans = {
    "M": ("1 Month", 199),
    "3": ("3 Months", 599),
    "Y": ("1 Year", 1999)
}

plan_details = {}

plan_month =  199
plan_months =  599
plan_year = 1999

user_name = input("Enter your name : ")
mobile_number = int(input("Enter mobile number : "))

plan_details['user_name'] = user_name
plan_details['mobile_number'] = mobile_number

recharge_plan = input("Enter your recharge plan(M,3 ,Y )").upper()

plan_details['recharge_plan'] = recharge_plan

payment_amount = int(input("Enter your payment amount : "))
plan_details['payment_amount'] = payment_amount

print("M → 1 Month ₹199")
print("3 → 3 Months ₹599")
print("Y → 1 Year ₹1999")

if recharge_plan not in plans :
     print("invalid recharge plan!!")

plan_name, plan_price = plans[recharge_plan]

plan_details['plan'] = plan_name
plan_details['plan_price'] = plan_price

booking_ID  = "BK" + str(random.randint(100000, 999999)) 
plan_details['booking_ID'] = booking_ID
plan_details['pending_balance'] = plan_details['plan_price'] - plan_details['payment_amount']

for key , value in plan_details.items():
    print(f"{key} : {value}")



