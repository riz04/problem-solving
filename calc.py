num_one = None
num_two = None
operator = None
result = None
is_operation_done = False
operator_list = ['+', '-', '/', 'x', 'X']

num_one = float(input("Enter first value: "))
num_two = float(input("Enter second value: "))

while (is_operation_done != True):
    operator = input("Choose an operator : +,-,x,/ \n")
    if (operator not in operator_list ):
        pass
    else:
        is_operation_done = True

if operator == '+':
    result = num_one + num_two
elif operator == '-':
    result = num_one - num_two
elif operator.lower() == 'x':
    result = num_one * num_two
else:
    result = num_one / num_two

print(f'Result of {num_one} {operator} {num_two} = {result} ')

    

