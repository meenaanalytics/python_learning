'''string slicing'''

# b = "hello/zo, world! hfereeerofjerjj fjflkejioewhu vishallllx"     #['h' , 'e' , 'l' , ... , ',' , ] 

# print(b[8:12])      # slicing from inbetween
# print(b[7:-1])      # slicing from practicular index to last -1 
# print(b[:5])        # slicing from start to perticular index
# print(b[2:])        # slicing from practicular index to last(included)

# print(b[-5:-2])     # negative selecting


# fruits = ['apple' , 'orange' , 'grapes' , 'watermelon']

# print(fruits[2:3])
# print(fruits[0:3])


'''string modification'''

movie_name = 'dilwale dulhaniya le jayege!'

# print(movie_name.upper())     #convert string to upper case
# print(movie_name.lower())     #convert string to lower case
# print(movie_name.strip())     #cut space from start and the end (ex:       dilwale dulhaniya le jayege!'    )
# print(movie_name.replace('d' , 'v'))      #to replace single letter
# print(movie_name.replace('dilwale' , 'love'))     #to replace the word
# print(movie_name.replace('dilwale dulhaniya le jayege!' , 'am so lonely broken angel'))     

# today_schedul = 'going for a walk, eat breakfast, go to office, do your job'

# print(today_schedul.split('o'))

'''string concatination'''

# var = 'hello'
# var1 = 'world'

# var4 = var + ' ' + var1 + 'vishal'

# print(var4)

'''format string'''


age = 36
bill = 500
# This will produce an error:
# txt = 'my name is jhon, i am ' + age ❌ wrong!!

# txt = f'my name is jhon, my bill is  {bill:.2f}'
# txt = f'my name is jhon, my bill is  {bill * 10}'

# print(f'{txt} {age}')
# print(txt)

'''escape character'''

# txt = "hello i am going for a movie today named : "bahubali"".❌ wrong!! gives you error
txt = "hello \bi am\t going \\for a \rmovie \ftoday \n named : \"bahubali\"" #✅ correct

print(txt)




