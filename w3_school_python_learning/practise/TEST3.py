'''wrt a program to print number from 1 to 5 using a for loop'''

# for i in range(1,6):
#     print(i, end=" ")


'''wrt a program to print the squares of numbers from 1 to 5 '''

# for i in range(1,6):
#     print(i ** 2, end=" ")


'''wrt a program to print all even number from 1 to 10'''

# for i in range(1, 11):
#     if i % 2 ==0:
#         print(i)


'''wrt a program to calculate the sum of numbers from 1 to 10'''

# total = 0

# for i in range(1,11):
#     total += i

# print(f"sum is {total}")


'''(5)..wrt a program to print the world "python" in reverse using a for loop '''

# word = 'javascript'

# for i in range(len(word) -1, -1, -1):
#     print(word[i], end=" ")

'''(6)..wrt a program to count the number of vowels in the word "education" '''

# vowels = "aeiou"
# word = "education"
# count = 0

# for char in word:
#     if char in vowels:
#         count +=1

# print(f"Total vowels in {word} is {count}")      

'''(7)..wrt a program tp print the first 10 items of the fibonacci sequence'''

# a = 0
# b = 1
# print(a, b, end=" ")
# #1 1 2

# for _ in range(10):
#     next_term = a + b
#     print(next_term, end=" ")
#     a,b = b , next_term


'''(8)..wrt a program to calculate the factorial of a give number , such as 5.
output=5
'''

# n = 5
# factorial = 1

# for i in range(1, n+1):
#     factorial *=1

# print(f"factorial of {n} is {factorial}")    

'''(9)..wrt a program to check if a given number , such as 7, is a prime number'''

# num = 7
# is_prime = True
 
# for i in range(2, int(25 ** 0.5) + 1):
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime and num > 1:
#     print(num, "is a prime member") 
# else:
#     print(num, "is not a prime member")       


'''(10)..wrt a prg to occurrences of each character in the word "programming" '''

# word = "programming"
# char_count = {}

# for char in word:
#     if char in char_count:
#         char_count[char] +=1
#     else:
#         char_count[char] = 1

# for char, count in char_count.items():
#     print(char + ':' , count)            