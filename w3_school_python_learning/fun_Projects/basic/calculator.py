'''
4 function add() , sub(), div(), mul()

1 main function main(Operation, *value)

'''

'''
Operation = 'ADD', 'SUB', 'DIV', 'MUL'

'''

def add(*vals):
    result = 0
    for val in vals:
        result += val
    return result


def sub(*vals):  # [4 , 5 ,  2]
    result = vals[0]          # start with first value
    for val in vals[1:]:      # subtract remaining
        result -= val
    return result


def div(*vals):
    print('Divide function runned !!')
    return vals[0] / vals[1]


def mul(*vals):
    result = vals[0]          # start with first value
    for val in vals[1:]:      # multiply remaining values
        result *= val
    return result

def main(Operation, *values):
    OPERATIONS = ['ADD', 'SUB', 'DIV', 'MUL']
    try:
        if type(Operation) != str or Operation not in OPERATIONS:
            raise Exception("Please enter a valid Type from these : 'ADD', 'SUB', 'DIV', 'MUL'")
        else:
            match Operation:
                case 'ADD':
                    return add(*values)
                case 'SUB':
                    return sub(*values)
                case 'DIV':
                    if len(values) > 2:
                        raise Exception('Only 2 numbers are allowed in Division!!!')
                    return div(*values)
                case 'MUL':
                    return mul(*values)
                case _:
                    raise Exception("Invalid Operation Type!")
    except Exception as e:
        print(e)


# output = main('ADD', 4 , 5, 2)
# print('add > ', output)   # 11

# output1 = main('SUB', 4 , 5, 2)
# print('sub > ', output1)  # -3  (4 - 5 - 2)

# output2= main('MUL', 4 , 5, 2)
# print('mul > ', output2)  # 40 (4 * 5 * 2)

# output3= main('DIV', 10, 5, 5)
# print('div > ', output3)  

# output4= main('Sandwich', 10, 5, 5)
# print('div > ', output4)  

while True:
    operation = input('Enter operation type: ')
    values = input('Enter values with comma seperation: ') # '5,6,7,8'

    values_list = values.split(",") # => ['5' , '6' , '7' , '8']
    # values = [int(v) for v in values_list] #=> [5,6,7,8]
    values = []

    for val in values_list:
        val_converted_to_int = int(val)
        values.append(val_converted_to_int)

    output = None

    output = main(operation, *values)
        
    print(output)
