'''String slicing...'''

# b = "Hell/zo, World! asdflkj vishalllXd" # => ['H', 'e', 'l', ... ,  ',' ,' ', ]

# print(b[8:12]) # slicing from inbetween
# print(b[7:-1]) # slice from perticular index to last - 1
# print(b[:5]).  # slice from start to perticular index
# print(b[2:]).  # slice from perticular index to last (included )

# print(b[-5:-2]) #negative selecting

# fruit = ['apple', 'orange', 'graphs', 'watermelon']

# print(fruit[0:3])

'''String modification'''

# movie_name = 'dilwale dulhaniya le jaenge!' 

# print(movie_name.upper()) # convert string to upper case
# print(movie_name.lower()) # convert string to lower case 
# print(movie_name.strip()). # cut space from start and the end (ex: '             dilwale dulhaniya le jaenge!     ')
# print(movie_name.replace('d', 'O')) # to replace single letter
# print(movie_name.replace('dilwale', 'chijjjiwale')) # to replace the word
# print(movie_name.replace('dilwale dulhaniya le jaenge', 'Dabangg')) # to replace the word

# today_schedule = 'Going for a walk, eat breakfast, go to office, do your job'

# print(today_schedule.split('o')) # convert the string to a list 

'''string concatination'''

# var = 'Hello'
# var1 = 'World!'

# var4 = var + ' ' + var1 + 'vishal'

# print(var4)


'''format string (f string)'''

# age = 36
# bill = 500
#This will produce an error:
# txt = "My name is John, I am " + age ❌ wrong !!!

# txt = f"My name is John, my bill is {bill:.2f}"
# txt = f"My name is John, my bill is {bill * 10}"

# print(f"{txt} {age}")
# print(txt)

'''escape character'''

# txt = "Hello i'm going for a movie today named : "Bahubali"". ❌ wrong!! gives you error
# txt = "Hello \r i'm \t going  \f for a\b movie \\ today \n named : \"Bahubali\"" # ✅ CORRECT

# print(txt)

'''Home work!!!'''

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string