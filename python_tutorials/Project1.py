"""
🎯 PROJECT TITLE: Mini Student & Shopping System (Beginner Python Revision)

📝 DESCRIPTION:
This program is designed to revise all the basic Python concepts in one small project.
It simulates a simple shopping system for students, where a user can:
- Enter their name and age
- Check voting eligibility using if/elif/else
- View and select fruits from a list
- Use a while loop to add items to their cart
- View special offers (tuple)
- Store their details in a dictionary
- Choose a payment method using match-case
- Perform string operations like upper, lower, length
- Get a final confirmation message

💡 CONCEPTS USED:
1. Input and Type Conversion (int, str, float)
2. Conditional Statements (if, elif, else)
3. Loops (for loop and while loop)
4. Match Case (Python 3.10+)
5. List operations (displaying fruits, adding to cart)
6. Tuple (displaying offers)
7. Dictionary (storing student details)
8. String Operations (upper, lower, len)
9. Basic logical thinking and control flow

✅ WHAT YOU SHOULD PRACTICE:
- Change the fruits or add more products
- Add discounts or price calculation
- Add multiple students (list of dictionaries)
- Add input validation
- Use f-strings creatively to display messages

🚀 PURPOSE:
To build confidence in basic Python programming by combining all beginner-level topics
into one practical, simple project that can be extended later.
"""

# name = input("Enter your name: ")
# age = int(input('Enter your age: '))

# if age < 18:
#     print(f"You can't Vote sorry , {name}")
# elif age >= 18:
#     print(f"You can Vote , {name}")
# else:
#     print(f"Invalid Voter ID , {name}")


fruits_bucket = ['apple', 'banana', 'graphes', 'pineapple', 'orange', 'lichi']

for fruit in fruits_bucket:
    print(f" -> {fruit}")

cart = []

while True:
    item = input("Enter fruit or if you are done then type done : ").lower()
    if item in fruits_bucket:
        cart.append(item)
        print(f"{item} added to your Cart!!", cart)
    elif item == 'done':
        print(f"Your cart : {cart} , kindly pay the bill & leave")
        break
    else:
        print(f"{item} not found in fruit_bucket")