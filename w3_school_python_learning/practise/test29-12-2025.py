# Take a number and print:

# "Positive"
# "Negative"
# "Zero"

# num = int(input("Enter a number : "))

# if num > 0:
#     print("number is positive")
# elif num == 0:
#     print("number is zero") 
# else:
#     print("number is negative")       


# 3️⃣ ATM Withdrawal System 🏦

# Ask:
# balance const (Balance = 5000)
# withdrawal amount (float(input('Enter withdrawl amount: ')))
# Conditions:
# If withdrawal > balance → "Insufficient balance"
# If amount ≤ 0 → "Invalid amount"
# If amount is not multiple of 100 → "Enter amount in multiples of 100"
# Else → "Collect cash"
# ⚠️ Order of conditions matters!

# total_balance = 200000

# withdrawal_amount = int(input('Enter withdrawal amount : '))

# # print(withdrawal_amount)

# if withdrawal_amount > total_balance:
#     print('Insufficient Balance!!!')
# elif withdrawal_amount <= 0:
#     print('Invalid amount!!!')
# elif withdrawal_amount % 100 != 0:
#     print('Enter amount in multiples of 100 !!!')
# else:
#     print('Collect cash!!')
#     total_balance -= withdrawal_amount
#     print(f"Available balance: {total_balance}")





# 7️⃣ Movie Ticket Pricing 🎬
# Ask:
# age
# show time ("morning", "evening")
# Rules:
# Children (<12): ₹100
# Adults:
# Morning → ₹150
# Evening → ₹200
# Senior citizens (≥60): 50% off

# showDict = {
#     'M': 'morning',
#     'E': 'evening'
# }

# child_ticket_price = 100
# adult_M_ticket_price = 150
# adult_E_ticket_price = 200

# senior_citizens_discount = 50 / 100 # 0.5

# age = int(input('Enter your age: '))

# show_time = input('Enter show time (type M for morning / E for evening show): ')

# if age < 12:
#     print(f'Your ticket price is ₹{child_ticket_price}')
# else:
#     if showDict[show_time] == 'morning':
#         if age >= 60:
#             print(f'Good morning!!!, Your ticket price is {adult_M_ticket_price * senior_citizens_discount}')
#         else:
#             print(f'Good morning!! Your ticket price is ₹{adult_M_ticket_price}')
#     else:
#         if age >= 60:
#             print(f'Good evening!!! Your ticket price is ₹{adult_E_ticket_price * senior_citizens_discount}')
#         else:
#             print(f'Good evening!! Your ticket price is ₹{adult_E_ticket_price}')



'''-------------------------------------------------------------------------'''


# 1️⃣ Check Positive or Negative
# Write a program to check whether a number is positive or negative.

# num = int(input("Enter a number : "))

# if num > 0:
#     print("Number is positive")
# elif num ==0:
#     print("Number is ZERO")  
# else:
#     print("Number is negative ")      



# 2️⃣ Check Even or Odd
# Take a number from the user and print Even or Odd.
# 💡 Hint: use % 2

# NUM = int(input("Enter a number : "))

# if NUM %2 == 0:
#     print("number is even")
# else:
#     print("number is odd")    



# 3️⃣ Age Check
# Ask the user’s age:
# If age ≥ 18 → "Allowed"
# Else → "Not allowed"

# age = int(input("Enter your age : "))

# if age >= 18:
#     print("you allowed")
# else:
#     print("you not allowed")    



# 4️⃣ Number Comparison
# Take two numbers as input from user and print which one is bigger.

# a = int(input("Enter a number :"))
# b = int(input("Enter a number :"))
 
# if a > b:
#     print("a")
# else:
#     print("b")    
 


# 5️⃣ Pass or Fail
# Ask marks from the user:
# If marks ≥ 40 → "Pass"
# Else → "Fail"

# marks = int(input("Enter the marks : "))

# if marks >= 40:
#     print("You are pass")
# else:
#     print("You are fail")    




#7️⃣ Movie Ticket Pricing 🎬
# Ask:
# age
# show time ("morning", "evening")
# Rules:
# Children (<12): ₹100
# Adults:
# Morning → ₹150
# Evening → ₹200
# Senior citizens (≥60): 50% off

# showDict = {
#     'M': 'morning',
#     'E': 'evening'
# }

# children_ticket_price = 100
# adult_M_ticket_price = 150
# adult_E_ticket_price = 200

# senior_citizen = 50 / 100

# age = int(input("Enter your age : "))

# show_time = str(input("Enter your show time(type M FOR morning , E for evening)"))

# if age < 12:
#     print("your ticket price is 100")
# else:
#     if showDict[show_time] == 'morning':
#        if age >= 60:
#         print(f"Good morning!!! your ticket price{adult_M_ticket_price * senior_citizen}") 
#        else:
#         print(f"Good morning!!! your ticket price{adult_M_ticket_price}")

#     else:
#         if age >=60:
#            print(f"Good evening!!! your ticket price{adult_E_ticket_price * senior_citizen}") 
#         else:
#           print(f"Good evening!!! your ticket price{adult_E_ticket_price}")       



# 6️⃣ Online Shopping Bill 🛒
# Ask:
# amount
# membership (yes / no)
# Rules:
# If amount ≥ 3000 → 20% off
# Else if amount ≥ 1000 → 10% off
# Members get extra 5% off
# 🧠 Apply discounts in correct order.


# def calculateBillAfterDiscount(discount_rate):
#     discount_value = amount * discount_rate
#     final_bill = amount - discount_value
#     return final_bill


# discount_above_3000 = 20 / 100 # 0.2
# discount_above_1000 = 10 / 100 # 0.1
# membership_discount = 5 / 100 #0.05

# final_discount = 0

# membershipObj = {
#     '0': 'NO',
#     '1': 'YES'
# }

# amount = float(input('Enter amount: '))
# membership = input("Do you have the membership (0 for NO, 1 for YES): ")

# if membershipObj[membership] == 'YES':
#     final_discount += membership_discount
#     print('Membership discount applied of 5%', final_discount)
#     if amount >= 3000:
#         final_discount += discount_above_3000
#         print(f'Your bill is total : {amount}, {final_discount * 100}% discount applied!!')
#         print(f'Your bill after discount: {calculateBillAfterDiscount(final_discount)}')
#     elif amount >= 1000:
#         final_discount += discount_above_1000
#         print(f'Your bill is total : {amount}, {final_discount * 100}% discount applied!!')
#         print(f'Your bill after discount: {calculateBillAfterDiscount(final_discount)}')

# else:
#     final_discount = 0
#     if amount >= 3000:
#         final_discount += discount_above_3000
#         print(f'Your bill is total : {amount}, {final_discount * 100}% discount applied!!')
#         print(f'Your bill after discount: {calculateBillAfterDiscount(final_discount)}')
#     elif amount >= 1000:
#         final_discount += discount_above_1000
#         print(f'Your bill is total : {amount}, {final_discount * 100}% discount applied!!')
#         print(f'Your bill after discount: {calculateBillAfterDiscount(final_discount)}')




'''removed duplicate lines using functions'''

# def calculateBillAfterDiscount(discount_rate):
#     discount_value = amount * discount_rate
#     final_bill = amount - discount_value
#     return final_bill

# def handleDiscountBasedonBill(amount, final_discount):
#     print(f'Your bill is total : {amount}, {final_discount * 100}% discount applied!!')
#     print(f'Your bill after discount: {calculateBillAfterDiscount(final_discount)}')


# discount_above_3000 = 20 / 100 # 0.2
# discount_above_1000 = 10 / 100 # 0.1
# membership_discount = 5 / 100 #0.05

# final_discount = 0

# membershipObj = {
#     '0': 'NO',
#     '1': 'YES'
# }

# amount = float(input('Enter amount: '))
# membership = input("Do you have the membership (0 for NO, 1 for YES): ")

# if membershipObj[membership] == 'YES':
#     final_discount += membership_discount
#     print('Membership discount applied of 5%', final_discount)
#     if amount >= 3000:
#         final_discount += discount_above_3000
#         handleDiscountBasedonBill(amount, final_discount)
#     elif amount >= 1000:
#         final_discount += discount_above_1000
#         handleDiscountBasedonBill(amount, final_discount)

# else:
#     final_discount = 0
#     if amount >= 3000:
#         final_discount += discount_above_3000
#         handleDiscountBasedonBill(amount, final_discount)
#     elif amount >= 1000:
#         final_discount += discount_above_1000
#         handleDiscountBasedonBill(amount, final_discount)



# 6️⃣ Online Shopping Bill 🛒
# Ask:
# amount
# membership (yes / no)
# Rules:
# If amount ≥ 3000 → 20% off
# Else if amount ≥ 1000 → 10% off
# Members get extra 5% off
# 🧠 Apply discounts in correct order.

def BillAfterDiscount(discount):
    discount_value = amount * discount
    final_discount = amount - discount_value
    return final_discount

amount = float(input("Enter amount : "))
membership = input("you have a membership(0 for NO , 1 for YES)")

discount_above_3000 = 20 / 100
discount_above_1000 = 10 / 100
membership_discount = 5 / 100

final_discount = 0

membershipObj = {
    '0' : 'NO',
    '1' : 'YES'
}

if membershipObj[membership] == 'YES':
    final_discount += membership_discount
    print("membership apply 5% discount-- ", final_discount)
    if amount >= 3000:
        final_discount += discount_above_3000
        print("apply your 20% discount--", final_discount * 100)
        print(f"your bill is : {amount} , {BillAfterDiscount(final_discount)}")
    elif amount >=1000:
        final_discount += discount_above_1000
        print(f"apply your 10% discount-- , final_discount")
        print(f"your bill is : {amount} , {BillAfterDiscount(final_discount)}")
else:
    if amount >= 3000:
        final_discount += discount_above_3000
        print("apply your 20% discount--", final_discount * 100)
        print(f"your bill is : {amount} , {BillAfterDiscount(final_discount)}")
    elif amount >=1000:
        final_discount += discount_above_1000
        print(f"apply your 10% discount-- , final_discount")
        print(f"your bill is : {amount} , {BillAfterDiscount(final_discount)}")