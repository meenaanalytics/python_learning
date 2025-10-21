MAX_SPEED = int(input('Enter your speed: '))

if MAX_SPEED < 80:
    print('You are safe buddy!!!')

elif MAX_SPEED > 80 and MAX_SPEED < 120:
    print('lower your speed for safty!!')

else:
    print('You reached the dead Zone speed!!!')

loop

for i in range(10):
    print(f"vishal {i} x {i} kumar = " , i * i)  # f - string ( formatted string literal )

"sldfal203948203949*^&*&*&^*&dfKJHKJ*787*&^%^5" ( a string is a collection of letters , words, symbols , number , etc within a double quote or single quote)

students = {
    'name': 'Jay',
    'class': '10th',
    'course': 'maths',
    'timing':'10-03'
}

print(students['timing'])


print(f"Hi my name is {students['name']}")

print(f"Hi my class is {students['class']}")

print(students.items())
for key, value in students.items():
    print(f"{key} - {value}")

colors = ['red', 'blue', 'purple', 'pink', 'yellow', 'orange']

for key in colors:
    print(f"{key}")

[ ('name', 'Vishal'), ('class', '10th'), ('course', 'maths'), ('timing', '10-03') ]

