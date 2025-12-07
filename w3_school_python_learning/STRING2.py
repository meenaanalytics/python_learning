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

age = 36
bill = 500
# This will produce an error:
# txt = "My name is John, I am " + age ❌ wrong !!!

# txt = f"My name is John, my bill is {bill:.2f}"
# txt = f"My name is John, my bill is {bill * 10}"

# print(f"{txt} {age}")
# print(txt)

'''escape character'''

# txt = "Hello i'm going for a movie today named : "Bahubali"". ❌ wrong!! gives you error
# txt = "Hello \r i'm \t going  \f for a\b movie \\ today \n named : \"Bahubali\"" # ✅ CORRECT

# print(txt)

'''HOME WORK!!!'''

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string


'''1..Converts the first character to upper ca'''

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


'''2..onverts string into lower case'''


# txt = "AM SO LONELY BROKEN ANGEL, LISTEN TO MY HEART."

# x = txt.casefold()

# print(x)


'''3..Returns a centered string'''


# txt = "ONE AND ONLY, BROKEN ANGEL"

# x = txt.center(80)

# print(x)


'''4..Returns the number of times a specified value occers in the string'''

txt = "COME AND SAVE ME BEFOR I FALL APART"

x = txt.count("A")

print('mmm',x)


'''5..Returns an encoded version of the string'''

txt = "YOU WERE THE SHADOW TO MY LIGHT, DID YOU FEEL US?"

x = txt.encode()

print('VVVV',x)


'''6..	Returns true if the string ends with the specified value'''

# txt = "ANOTHER STAR , YOU FADE AWAY"

# x = txt.endswith("V")

# y = txt.endswith("Y")

# print(y)
# print(x)


'''7..Sets the tab size of the string'''

# txt = "afarid our aim is out of sight , wanna see us , alight"

# x = txt.expandtabs()

# print(x)


'''8..Searches the string for a specified value and returns the position of where it was found'''

txt = "ONE AND ONLY, BROKEN ANGEL"

x = txt.find("ANGEL")

print('XXXX ', x)


''' 9..	Formats specified values in a string'''


# txt = "COME {} SAVE ME BEFOR {} FALL APART"

# x = txt.format("AND "," I ")

# print(x)


'''10..Formats specified values from a dictionary in a string'''

# txt = {"NAME" : "LOVE" , "SAVE ME BEFOR" :   "YOU"}

# name = "my name is {NAME} and i live in {SAVE ME }"

# x = name.format_map(txt)

# print(x)


'''11Searches the string for a specified value and returns the position of where it was found'''


txt = "ONE AND ONLY, BROKEN ANGEL"

x = txt.index("D")

print(x)



